"""Local embeddings-only compatibility adapter with a finite setup budget."""
from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler
from pathlib import Path
import json
import os
import secrets
import threading
import urllib.request
import urllib.error

ROOT = Path(__file__).resolve().parents[1]
KEY = ROOT / "state/authority/voyage.key"
TOKEN = ROOT / "state/authority/embedding-local.token"
BUDGET = ROOT / "state/embedding-budget.json"
LOCK = threading.Lock()
MAX_BYTES = int(os.environ.get("HERMES_UDR_EMBEDDING_MAX_INPUT_BYTES", "1000000"))

class Handler(BaseHTTPRequestHandler):
    def log_message(self, *args):
        pass

    def respond(self, status, value):
        payload = json.dumps(value).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)

    def do_GET(self):
        self.respond(200, {"model": "voyage-4-large", "dimension": 1024,
            "provider": "voyage", "setup_budget_input_bytes": MAX_BYTES if MAX_BYTES>0 else None, "budget_mode": "enforce" if MAX_BYTES>0 else "observe"})

    def do_POST(self):
        if self.path != "/v1/embeddings" or not secrets.compare_digest(
                self.headers.get("Authorization", ""), "Bearer " + TOKEN.read_text().strip()):
            self.respond(403, {"error": "denied"}); return
        size = int(self.headers.get("Content-Length", "0"))
        if not 0 < size <= 131072:
            self.respond(413, {"error": "input_limit"}); return
        data = json.loads(self.rfile.read(size))
        texts = data.get("input")
        texts = [texts] if isinstance(texts, str) else texts
        if not isinstance(texts, list) or not 0 < len(texts) <= 64 or any(not isinstance(t, str) for t in texts):
            self.respond(400, {"error": "text_input_required"}); return
        if data.get("model") != "voyage-4-large" or data.get("dimensions", 1024) != 1024:
            self.respond(400, {"error": "embedding_schema_mismatch"}); return
        upper = sum(len(t.encode()) + 256 for t in texts)
        with LOCK:
            budget = json.loads(BUDGET.read_text()) if BUDGET.exists() else {"reserved_input_bytes": 0, "actual_tokens": 0}
            if MAX_BYTES > 0 and budget["reserved_input_bytes"] + upper > MAX_BYTES:
                self.respond(429, {"error": "setup_budget_exhausted"}); return
            budget["reserved_input_bytes"] += upper
            BUDGET.write_text(json.dumps(budget))
        body = {"input": texts, "model": "voyage-4-large", "output_dimension": 1024,
            "output_dtype": "float", "truncation": False}
        if data.get("input_type") in ("query", "document"):
            body["input_type"] = data["input_type"]
        request = urllib.request.Request("https://api.voyageai.com/v1/embeddings",
            data=json.dumps(body).encode(), headers={"Authorization": "Bearer " + KEY.read_text().strip(),
            "Content-Type": "application/json"})
        try:
            with urllib.request.urlopen(request, timeout=45) as response:
                result = json.load(response)
        except urllib.error.HTTPError as exc:
            self.respond(exc.code, {"error": "provider_rejected", "status": exc.code}); return
        vectors = result["data"]
        if len(vectors) != len(texts) or any(len(v["embedding"]) != 1024 for v in vectors):
            self.respond(502, {"error": "provider_dimension_mismatch"}); return
        with LOCK:
            budget = json.loads(BUDGET.read_text())
            budget["actual_tokens"] += result.get("usage", {}).get("total_tokens", 0)
            BUDGET.write_text(json.dumps(budget))
        self.respond(200, result)

if __name__ == "__main__":
    for path in (KEY, TOKEN):
        if path.is_symlink() or path.stat().st_mode & 0o077:
            raise SystemExit("private_key_file_required")
    ThreadingHTTPServer(("127.0.0.1", 62491), Handler).serve_forever()
