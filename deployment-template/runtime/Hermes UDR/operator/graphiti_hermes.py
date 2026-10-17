"""Graphiti factory adapter; pinned upstream files remain unchanged."""
import asyncio
import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "software/graphiti/mcp_server"
sys.path.insert(0, str(SOURCE / "src"))
from graphiti_core.llm_client.client import LLMClient
from graphiti_core.llm_client.config import LLMConfig
from services.factories import LLMClientFactory

class HermesOAuthLLM(LLMClient):
    def __init__(self):
        super().__init__(LLMConfig(model="gpt-6.1-sol", small_model="gpt-6.1-sol", max_tokens=128000))
        self.calls = 0

    async def _generate_response(self, messages, response_model=None, max_tokens=128000, model_size=None):
        limit = int(os.environ.get("HERMES_UDR_GRAPHITI_MAX_CALLS", "0"))
        if limit and self.calls >= limit:
            raise RuntimeError("graphiti_installation_inference_budget_exhausted")
        self.calls += 1
        prompt = json.dumps([m.model_dump() for m in messages], ensure_ascii=False)
        if response_model is not None:
            prompt += "\nReturn a JSON object conforming to: " + json.dumps(response_model.model_json_schema())
        process = await asyncio.create_subprocess_exec(
            str(ROOT / "software/hermes/.venv/bin/python"),
            str(ROOT / "operator/hermes_llm_worker.py"),
            stdin=asyncio.subprocess.PIPE, stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.DEVNULL, cwd=str(ROOT / "workspace"),
        )
        try:
            out, _ = await asyncio.wait_for(process.communicate(json.dumps({"prompt": prompt,
                "max_tokens": 128000 if os.environ.get("HERMES_UDR_INFERENCE_BUDGET_MODE")=="observe" else max_tokens}).encode()), timeout=900 if os.environ.get("HERMES_UDR_INFERENCE_BUDGET_MODE")=="observe" else 260)
        except BaseException:
            if process.returncode is None:
                process.kill()
                await process.wait()
            raise
        if process.returncode:
            raise RuntimeError("hermes_oauth_inference_failed")
        result = json.loads(out)
        if result.get("completed") is not True:
            raise RuntimeError("hermes_oauth_inference_incomplete")
        value = result["value"]
        if response_model is not None:
            value = response_model.model_validate(value).model_dump()
        usage = {k: v for k, v in result.items() if k != "value"}
        with (ROOT / "operator/receipts/graphiti-native-inference.jsonl").open("a") as f:
            f.write(json.dumps(usage) + "\n")
        return value

def create(config):
    if config.model != "gpt-6.1-sol":
        raise ValueError("model_policy")
    return HermesOAuthLLM()

LLMClientFactory.create = staticmethod(create)

if __name__ == "__main__":
    from graphiti_mcp_server import main
    main()
