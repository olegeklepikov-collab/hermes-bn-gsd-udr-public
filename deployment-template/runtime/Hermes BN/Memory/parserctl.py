"""Operator CLI for the same mandatory isolated parser used by ordinary Hermes and UDR."""
from pathlib import Path
import json,sys,runpy
cfg=json.loads((Path(__file__).parent/'settings.json').read_text());sys.path.insert(0,cfg['package_root'])
sys.argv=[sys.argv[0],'--python',cfg['document_python'],*(['--xls-java',cfg['xls_java']] if cfg.get('xls_java') else []),*sys.argv[1:]]
runpy.run_module('bn_memory.parser_cli',run_name='__main__')
