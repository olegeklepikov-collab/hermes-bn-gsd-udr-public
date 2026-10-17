"""Operator-owned exact catalogue, bound to actual configured MCP transports."""
from pathlib import Path
import hashlib
from .codec import canonical,read_json,digest


def transport_digest(config):
    return digest(config)


class ToolPolicy:
    def __init__(self,settings):
        self.settings=settings
        path=Path(settings['tool_policy'])
        if hashlib.sha256(path.read_bytes()).hexdigest()!=settings['tool_policy_sha256']:raise ValueError('Tool admission policy changed')
        self.policy=read_json(path.read_bytes())
        for name,sha in settings.get("local_adapter_sha256",{}).items():
            if hashlib.sha256(Path(name).read_bytes()).hexdigest()!=sha:raise ValueError("Admitted local adapter changed: "+name)
        if self.policy.get('version')!=1:raise ValueError('Unknown tool policy')
    def classify(self,name,args):
        row=self.policy['entries'].get(name)
        if not row:return None
        from hermes_cli.config_effective import load_user_config_effective
        config=load_user_config_effective().get('mcp_servers',{}).get(row['server'])
        if not config or transport_digest(config)!=self.settings['mcp_transport_digests'].get(row['server']):
            raise ValueError('MCP transport/config changed; owner admission required')
        from tools import mcp_tool
        # Provenance is captured by the native registry, never inferred from a model-supplied name.
        if mcp_tool._mcp_tool_server_names.get(name)!=row['server']:
            raise ValueError('Registered MCP provenance does not match the admitted server')
        if len(canonical(args))>262144:raise ValueError('Tool input exceeds admitted bound; split independent work')
        return row
