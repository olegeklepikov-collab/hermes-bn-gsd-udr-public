from pathlib import Path
import json,urllib.request
from huggingface_hub import snapshot_download
z=Path(__file__).resolve().parents[1]
manifest={}
patterns=['config.json','model.safetensors','model.safetensors.index.json','model-*.safetensors','modules.json','config_sentence_transformers.json','sentence_bert_config.json','1_Pooling/config.json','tokenizer.json','tokenizer_config.json','special_tokens_map.json','sentencepiece.bpe.model','vocab.txt','README.md']
for name in ['intfloat/multilingual-e5-large','mixedbread-ai/mxbai-embed-large-v1']:
 d=json.load(urllib.request.urlopen('https://huggingface.co/api/models/'+name));rev=d['sha'];print('Downloading',name,rev,flush=True)
 path=snapshot_download(name,revision=rev,allow_patterns=patterns,max_workers=2,token=False)
 manifest[name]={'revision':rev,'path':path,'license':d.get('cardData',{}).get('license'),'safetensors':True}
 (z/'config/model-snapshots.json').write_text(json.dumps(manifest,indent=2))
 print('Ready',name,flush=True)
