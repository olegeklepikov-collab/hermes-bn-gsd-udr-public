import argparse,asyncio,json,sys
from pathlib import Path
from api import P,load,save,request,save_images

parser=argparse.ArgumentParser(prog='r-bn')
parser.add_argument('command',choices=['status','profiles','catalog','call','batch','run'])
parser.add_argument('--name')
parser.add_argument('--profile')
parser.add_argument('--params',type=Path)
parser.add_argument('--code-file',type=Path)
parser.add_argument('--output',type=Path)
parser.add_argument('--image-dir',type=Path)
args=parser.parse_args()
try:
    params=load(args.params) if args.params else {}
    profiles=load(P/'config/profiles.json') if (P/'config/profiles.json').exists() else {}
    if args.profile:
        profile=profiles[args.profile]
        args.command='call'
        args.name=profile['name']
        params={**profile.get('arguments',{}),**params}
    if args.command=='run':
        if not args.code_file:
            raise ValueError('Для run требуется --code-file.')
        args.command='call'
        args.name='btw_tool_run_r'
        params={'code':args.code_file.read_text(),'_intent':'Выполнить предоставленный файл R'}
    if args.command=='status':
        result={'mode':'local','api_key_used':False,'R_runtime':'__HERMES_BN_R_RUNTIME__/env',
                'profiles':len(profiles),'verification':load(P/'config/verification.json') if (P/'config/verification.json').exists() else {}}
    elif args.command=='profiles':
        result=profiles
    else:
        result=asyncio.run(request(args.command,args.name,params))
    if args.image_dir:
        print('images',json.dumps(save_images(result,args.image_dir),ensure_ascii=False))
    if args.output:
        save(args.output,result)
        print(args.output)
    else:
        print(json.dumps(result,ensure_ascii=False,indent=2))
    if result.get('ok') is False or result.get('isError'):
        sys.exit(2)
except Exception as error:
    while isinstance(error,BaseExceptionGroup) and error.exceptions:
        error=error.exceptions[0]
    print(json.dumps({'ok':False,'error_type':type(error).__name__,'error':str(error)[:2000]},ensure_ascii=False),file=sys.stderr)
    sys.exit(2)
