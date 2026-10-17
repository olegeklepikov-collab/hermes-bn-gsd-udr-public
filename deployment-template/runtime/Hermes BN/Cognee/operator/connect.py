"""Connect the separate tested SDK to all native BN profiles, preserving old policies."""
from pathlib import Path
import hashlib,json,os,shutil,sys,yaml
C=Path(__file__).resolve().parents[1];B=C.parent;M=B/'Memory';version=sys.argv[1] if len(sys.argv)>1 and sys.argv[1]!='rollback' else Path(json.loads((M/'settings.json').read_text())['package_root']).name;release=M/'releases'/version
def digest(value):return hashlib.sha256(json.dumps(value,ensure_ascii=False,sort_keys=True,separators=(',',':'),allow_nan=False).encode()).hexdigest()
def write(path,text):
    temp=path.with_name(path.name+'.cognee-connect.tmp');temp.write_text(text);temp.chmod(0o600);os.replace(temp,path)
def main():
    if not release.is_dir():raise RuntimeError('Requested qualified memory release is absent; do not copy historical staging code')
    cfg=json.loads((M/'settings.json').read_text());cfg.update({'package_root':str(release),'cognee_root':str(C),'cognee_enabled':True,'cognee_lesson_enabled':True});write(M/'settings.json',json.dumps(cfg,ensure_ascii=False,indent=2))
    sys.path.insert(0,str(release));from bn_memory.schemas import SCHEMAS
    server={'command':cfg['python'],'args':[str(release/'bn_memory/server.py'),str(M/'settings.json')],'enabled':True,'timeout':360}
    homes=[B/'data',B/'data/profiles/bn-gsd-only',B/'data/profiles/bn-udr-only']
    for home in homes:
        config=yaml.safe_load((home/'config.yaml').read_text());config['mcp_servers']['context']=dict(server)
        for surface,names in config.get('platform_toolsets',{}).items():
            if isinstance(names,list) and 'context' not in names:names.append('context')
        write(home/'config.yaml',yaml.safe_dump(config,allow_unicode=True,sort_keys=False))
        p=home/'plugins/bn-common-memory/plugin.yaml';manifest=yaml.safe_load(p.read_text());manifest['version']=version;write(p,yaml.safe_dump(manifest,allow_unicode=True,sort_keys=False))
    for p in [B/'GSD/operator/settings.json',B/'data/profiles/bn-gsd-only/settings.json']:
        d=json.loads(p.read_text());policy_path=Path(d['tool_policy']);policy=json.loads(policy_path.read_text())
        for name in SCHEMAS:policy['entries']['mcp__context__'+name]={'server':'context','mode':'audited_adapter'}
        write(policy_path,json.dumps(policy,ensure_ascii=False,indent=2));d['tool_policy_sha256']=hashlib.sha256(policy_path.read_bytes()).hexdigest();d['mcp_transport_digests']['context']=digest(server)
        for path in [M/'settings.json',release/'manifest.json',C/'operator/knowledge-work.owl',*(release/'bn_memory').glob('*.py')]:d['local_adapter_sha256'][str(path)]=hashlib.sha256(path.read_bytes()).hexdigest()
        write(p,json.dumps(d,ensure_ascii=False,indent=2))
    for p in [B/'data/plugins/bn-udr-host/__init__.py',B.parent/'Hermes UDR/operator/bn-bridge/plugin/__init__.py']:
        t=p.read_text();start=t.index("        if self.independent and name.startswith('mcp__context__'):");stop=t.index("        if self.independent:\n            return ExecutionDecision(name in",start)
        t=t[:start]+"        if self.independent and name.startswith('mcp__context__'):\n            return ExecutionDecision(name.removeprefix('mcp__context__') in "+repr(tuple(sorted(SCHEMAS)))+", 'Common memory uses its own mandatory scope controller')\n"+t[stop:];write(p,t)
    # Seal the final UDR host code after updating its allowed context tools.
    for settings_path in [B/'GSD/operator/settings.json',B/'data/profiles/bn-gsd-only/settings.json']:
        settings=json.loads(settings_path.read_text())
        for source_path in [B/'data/plugins/bn-udr-host/__init__.py',B.parent/'Hermes UDR/operator/bn-bridge/plugin/__init__.py']:
            settings['local_adapter_sha256'][str(source_path)]=hashlib.sha256(source_path.read_bytes()).hexdigest()
        write(settings_path,json.dumps(settings,ensure_ascii=False,indent=2))
    skill='''---\nname: cognee-knowledge-work\ndescription: Cognee в общей памяти всего Hermes BN: первичные источники, предметный граф, поиск, сводки и долговременные уроки.\n---\n\n1. Используй инструменты сервера context. Описания запрашивай группами до 10 имён. knowledge_ingest принимает только одну разрешённую запись record_id или относительный path, явную область task/project/owner и request_id. Для больших материалов задавай offset/length; полного чтения по фрагменту не заявляй. Оригинал и SHA сохраняются до обработки; модельные шаги выполняют настоящие листовые агенты Hermes, без инструментов и рекурсии.\n2. knowledge_query возвращает только адресный контекст (chunks/hybrid/graph/temporal/summaries), не окончательный ответ. source_quotes сверены с первичным текстом; graph context остаётся model_graph_unreviewed. При превышении размера читай context_ref через knowledge_manage(read_context), последовательно по offset.\n3. Общий memory_recall(mode=hybrid) включает Cognee как дополнительный индекс. Не записывай результат поиска как независимое новое свидетельство. GSD проверяет выводы; UDR хранит оригиналы, договор работы и научное принятие.\n4. knowledge_manage(enrich) строит сводки и возвращает фактические стадии. knowledge_manage(lesson,record_id,request_id,scope) обрабатывает явно сохранённое свидетельство. Типизированная запись trace поддерживает фактически выполненное действие; произвольную ошибку не выдумывай. Исходник и все части сохраняются, пределы SDK учитываются до записи. Отбор сохраняет исходные пороги уверенности и научный статус unreviewed. candidate_record_ids читай через memory_read; повторный request_id возвращает прежний результат. Отказы и превышения закрывают зависимый путь. no_accepted_lessons/skipped не означают созданный урок. Эти результаты — непроверенные производные, не новые правила исполнения.\n5. knowledge_manage(read_source,doc_id) повторно читает сохранённый текст; forget удаляет только указанную производную, сохраняя первичный оригинал. Дочерние роли могут читать, но не строить, менять или обогащать.\n6. Cognee имеет собственный конечный предел и общий ресурс родителя. При ошибке останови зависимую обработку, сохрани частичное состояние и причину. Отказ Cognee не означает отказ первичной памяти; не обходи обязательные контроллеры и не запускай второй управляющий цикл.\n'''
    for home in homes:
        d=home/'skills/cognee-knowledge-work';d.mkdir(parents=True,exist_ok=True);(d/'SKILL.md').write_text(skill)
    p=B/'workspace/AGENTS.md';t=p.read_text()
    if '## Cognee' not in t:t+='\n\n## Cognee\n\nCognee подключён ко всей общей памяти BN. Для предметного графа материалов, поиска по связям, сводок и долговременных уроков используй навык cognee-knowledge-work и инструменты knowledge_ingest/query/manage сервера context. Не создавай другую систему задач или второй исследовательский цикл. Родитель сохраняет области, ресурс и происхождение; дочерние роли — только чтение. Первичные источники и научное принятие остаются в SQLite/UDR/GSD.\n';write(p,t)
    (C/'checks/connection.json').write_text(json.dumps({'memory_version':version,'profiles':[h.name for h in homes],'tools':list(SCHEMAS),'native_models_required':True,'core_changed':False,'vendor_changed':False},indent=2));print('Cognee native integration connected to all three BN profiles')
def rollback():
    root=C/'operator/checkpoint-before-integration';entries=json.loads((root/'manifest.json').read_text())
    for item in entries:
        src=root/item['copy']
        if hashlib.sha256(src.read_bytes()).hexdigest()!=item['sha256']:raise RuntimeError('cognee_rollback_checkpoint_corrupt')
        shutil.copy2(src,item['path'])
    for home in [B/'data',B/'data/profiles/bn-gsd-only',B/'data/profiles/bn-udr-only']:
        p=home/'skills/cognee-knowledge-work'
        if p.exists():shutil.rmtree(p)
    print('Memory1.0.3 configuration restored; new originals and Cognee states retained; restart BN gateway')
if __name__=='__main__':rollback() if sys.argv[1:]==['rollback'] else main()
