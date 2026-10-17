from pathlib import Path
import json,sys
def register(ctx):
    config=ctx.get_config("config_file")
    root=json.loads(Path(config).read_text())["package_root"]
    sys.path.insert(0,root)
    from bn_memory.plugin import register as setup
    setup(ctx)
