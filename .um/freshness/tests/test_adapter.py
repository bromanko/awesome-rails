import hashlib
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
import ci,checks,history


def data(text):
    return dict(entries=ci.entries(text),readme=text,readmeHash=hashlib.sha256(text.encode()).hexdigest(),catalogSha='a'*40,slice=0,sliceCount=1)

def row(entry,**kw):
    result=dict(id=entry['id'],action='update',reason='Official source changed.',evidence=[dict(url='https://example.org/source',observation='Current source')],blockers=[],limitations=[],newName=None,newUrl=None,newDescription='Updated. - [Site](https://example.org)')
    result.update(kw);return result

class AdapterTests(unittest.TestCase):
    def test_native_formats_and_reference_resolution(self):
        rows=ci.entries('# Apps\n- [A](https://a.org) - Desc. - [Site](https://site.org)\n-[B](https://b.org)\n- [C][ref] - Text\n| [D](https://d.org)| yes | no |\n[ref]: https://c.org\n- [TOC](#apps)\n')
        self.assertEqual([x['name'] for x in rows],['A','B','C','D'])
        self.assertEqual(rows[2]['url'],'https://c.org')
        self.assertEqual(rows[0]['description'],'Desc. - [Site](https://site.org)')
        self.assertTrue(rows[3]['table'])
    def test_reference_name_update_does_not_rewrite_definition(self):
        d=data('- [Old][source] - Desc.\n[source]: https://source.org\n')
        r=row(d['entries'][0],newName='New',newDescription=None)
        p,_=ci.previews(d,dict(results=[r]),'unchanged')
        self.assertIn('[New](https://source.org)',p[0]['patch'])
        self.assertNotIn('-[source]:',p[0]['patch'])
    def test_rename_preserves_order(self):
        d=data('- [Z](https://z.org) - First.\n- [A](https://a.org) - Second.\n')
        raw=dict(results=[row(d['entries'][0],newName='B',newDescription=None),row(d['entries'][1],action='keep',newDescription=None)])
        p,_=ci.previews(d,raw,'unchanged')
        self.assertIn('+- [B]',p[0]['patch']);self.assertNotIn('-- [A]',p[0]['patch'])
    def test_table_description_is_held_but_url_can_change(self):
        d=data('| [D](https://d.org)| yes | no |\n')
        self.assertEqual(ci.previews(d,dict(results=[row(d['entries'][0])]),'unchanged')[0],[])
        p,_=ci.previews(d,dict(results=[row(d['entries'][0],newUrl='https://new.org',newDescription=None)]),'unchanged')
        self.assertIn('| [D](https://new.org)| yes | no |',p[0]['patch'])
    def test_parenthesized_existing_label_allows_description_correction(self):
        d=data('- [coderwall (legacy)](https://example.org) - Original.\n')
        p,_=ci.previews(d,dict(results=[row(d['entries'][0],newDescription='Corrected.')]),'unchanged')
        self.assertIn('+- [coderwall (legacy)](https://example.org) - Corrected.',p[0]['patch'])
        with self.assertRaises(ValueError):
            ci.previews(d,dict(results=[row(d['entries'][0],newName='bad](injected')]),'unchanged')
    def test_stale_catalog_and_blockers_hold(self):
        d=data('- [A](https://a.org) - Original.\n')
        r=row(d['entries'][0])
        self.assertEqual(ci.previews(d,dict(results=[r]),'changed')[0],[])
        r['blockers']=['Unverified version'];self.assertEqual(ci.previews(d,dict(results=[r]),'unchanged')[0],[])
    def test_newlines_rejected(self):
        d=data('- [A](https://a.org) - Original.\n')
        with self.assertRaises(ValueError):ci.previews(d,dict(results=[row(d['entries'][0],newDescription='x\nmalicious')]),'unchanged')
    def test_missing_link_success_holds(self):
        d=data('- [A](https://a.org) - Original.\n');p,_=ci.previews(d,dict(results=[row(d['entries'][0])]),'unchanged')
        original=checks.run
        def fake(cmd,*args,**kw):
            if cmd[0]=='lychee':return dict(exitCode=0,stdout='{}',stderr='')
            return original(cmd,*args,**kw)
        with tempfile.TemporaryDirectory() as tmp,patch.object(checks,'run',side_effect=fake):
            v=checks.Validator(Path(tmp),'a'*40,d['readme'],Path(tmp)/'logs')
            try:self.assertFalse(v.validate(p[0],d['entries'][0])['passed'])
            finally:v.close()
    def test_unavailable_history_holds(self):
        self.assertFalse(history.gate(dict(complete=False,errors=['rate limit']),None)[0])
    def test_exact_selected_coverage(self):
        d=data('- [A](https://a.org) - Original.\n')
        with self.assertRaises(ValueError):ci.validate(d,dict(results=[]))

if __name__=='__main__':unittest.main()
