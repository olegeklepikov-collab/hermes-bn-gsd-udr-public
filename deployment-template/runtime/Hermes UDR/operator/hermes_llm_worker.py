"""One bounded inference through the installed Hermes executor, without tools."""
import contextlib
import io
import json
import sys
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "software/hermes"))

def main():
    request = json.loads(sys.stdin.read(524289))
    prompt = request["prompt"]
    if len(prompt.encode()) > 524288:
        raise ValueError("input_limit")
    with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
        from hermes_cli.runtime_provider import resolve_runtime_provider
        from hermes_constants import parse_reasoning_effort
        from run_agent import AIAgent
        route = resolve_runtime_provider(requested="openai-codex", target_model="gpt-6.1-sol")
        agent = AIAgent(
            model="gpt-6.1-sol", provider=route["provider"],
            requested_provider="openai-codex", base_url=route["base_url"],
            api_key=route["api_key"], api_mode=route.get("api_mode"),
            credential_pool=route.get("credential_pool"),
            reasoning_config=parse_reasoning_effort("high"),
            enabled_toolsets=[], max_iterations=sys.maxsize if os.environ.get("HERMES_UDR_INFERENCE_BUDGET_MODE")=="observe" else 1, quiet_mode=True,
            skip_context_files=True, skip_memory=True, skip_background_review=True,
            max_tokens=min(int(request.get("max_tokens", 128000)), 128000),
            request_overrides={"reasoning":{"effort":"high"}},
            run_budget_seconds=None if os.environ.get("HERMES_UDR_INFERENCE_BUDGET_MODE")=="observe" else 240,
            ephemeral_system_prompt="Return only the JSON object requested. No Markdown. No tools.",
        )
        try:
            if agent.tools:
                raise RuntimeError("unexpected_tool_authority")
            result = agent.run_conversation(prompt)
        finally:
            agent.close()
    if result.get("failed") or not result.get("completed"):
        raise RuntimeError("inference_incomplete")
    value = json.loads(result["final_response"])
    if not isinstance(value, dict):
        raise ValueError("object_required")
    print(json.dumps({"value": value, "model": result.get("model"),
        "provider": result.get("provider"), "reasoning_effort": "high",
        "api_calls": result.get("api_calls"), "completed": True}, ensure_ascii=False))

if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(json.dumps({"failed": True, "error_type": type(exc).__name__}))
        raise SystemExit(1)
