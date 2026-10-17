import hashlib
import json
import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from bn_memory.store import Store
from bn_memory.plugin import Host
from bn_memory.broker import Broker

class HostTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();r=Path(self.tmp.name);(r/'project').mkdir()
        source=Path(__file__).parents[1]
        self.config={'package_root':str(source),'state_root':str(r/'state'),'default_project':'p','projects':{'p':str(r/'project')},'host_key':str(r/'key'),'context_bytes':2000}
        (r/'key').write_bytes(os.urandom(32));self.path=r/'config.json';self.path.write_text(json.dumps(self.config));Store(r/'state',self.config).initialize();self.host=Host(self.path)
    def tearDown(self):self.tmp.cleanup()
    def test_final_context_and_missing_context_block(self):
        self.host.before_turn(session_id='parent',user_message='Question',turn_id='t')
        request={'messages':[{'role':'user','content':'Question'}]};changed=self.host.request(request,session_id='parent')['request']
        self.assertTrue(self.host.model_control({'request':changed},session_id='parent').allow)
        self.assertFalse(self.host.model_control({'request':request},session_id='parent').allow)
        self.host.store.path.rename(self.host.store.path.with_suffix('.off'))
        self.assertFalse(self.host.model_control({'request':changed},session_id='parent').allow)
    def test_signed_tool_and_child_restriction(self):
        self.host.before_turn(session_id='parent',user_message='Question',turn_id='t');self.host.child_start(parent_session_id='parent',child_session_id='child')
        name='mcp__context__memory_record';args={'content':'x'}
        signed=self.host.tool_request(name,args,session_id='parent')['args']
        self.assertTrue(self.host.tool_control({'tool_name':name,'args':signed},session_id='parent').allow)
        self.assertFalse(self.host.tool_control({'tool_name':name,'args':signed},session_id='child').allow)
        signed['content']='tampered';self.assertFalse(self.host.tool_control({'tool_name':name,'args':signed},session_id='parent').allow)
    def test_optional_backends_fail_with_primary_results(self):
        self.host.store.bind('parent');self.host.store.record('parent',{'content':'Atlas originals SQLite','source_ref':'test:synthetic','kind':'note','request_id':'one','scope':'project'})
        with patch.object(self.host.broker,'worker',side_effect=RuntimeError('unavailable')),patch.object(self.host.broker,'embedding',side_effect=RuntimeError('unavailable')):
            r=self.host.broker.recall('parent',{'query':'Atlas','mode':'hybrid'});self.assertEqual(len(r['records']),1);self.assertTrue(all(x['status']=='unavailable' for x in r['derived'].values()))

if __name__=='__main__':unittest.main()
