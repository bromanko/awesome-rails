"""Check bounded README patches without imposing another catalog's lint rules."""
import json
import os
from pathlib import Path
import re
import subprocess
import tempfile
import ci


def run(command,cwd,env,timeout=180):
    try:
        r=subprocess.run(command,cwd=cwd,env=env,text=True,capture_output=True,timeout=timeout)
        return dict(exitCode=r.returncode,stdout=r.stdout,stderr=r.stderr)
    except (OSError,subprocess.TimeoutExpired) as e:
        return dict(exitCode=-1,stdout='',stderr=type(e).__name__+': '+str(e))


class Validator:
    def __init__(self,repo,sha,readme,output):
        self.repo,self.sha,self.readme,self.output=repo,sha,readme,output
        self.temp=tempfile.TemporaryDirectory(prefix='rails-freshness-')
        self.root=Path(self.temp.name)
        self.env={k:os.environ[k] for k in ('PATH','LANG','SSL_CERT_FILE','NIX_SSL_CERT_FILE') if k in os.environ}
        token=os.environ.get('FRESHNESS_GITHUB_TOKEN')
        if token:self.env['GITHUB_TOKEN']=token
    def close(self):self.temp.cleanup()
    def validate(self,proposal,entry):
        folder=self.root/('entry-'+proposal['id']);folder.mkdir()
        (folder/'README.md').write_text(self.readme)
        patch=folder/'change.patch';patch.write_text(proposal['patch'])
        logs={}
        for phase,command in [('applyCheck',['git','apply','--check',str(patch)]),('apply',['git','apply',str(patch)])]:
            logs[phase]=run(command,folder,self.env)
            if logs[phase]['exitCode']!=0:return dict(passed=False,reason='Patch does not apply to the pinned README.',logs=logs)
        changed=(folder/'README.md').read_text()
        if ci.patch_text(self.readme,changed)!=proposal['patch']:
            return dict(passed=False,reason='Applied change differs from proposal.')
        try:
            before,after=ci.entries(self.readme),ci.entries(changed)
            old=[e['line'] for e in before];new=[e['line'] for e in after]
            removed=[line for line in old if line not in new];added=[line for line in new if line not in old]
            if removed!=[entry['line']] or len(added)>1:raise ValueError('Expected one entry correction')
            relevant=[]
            if added:
                newentry=next(e for e in after if e['line']==added[0])
                relevant=[newentry['url']]+re.findall(r'\]\((https?://[^)]+)\)',newentry['description'])
        except (ValueError,StopIteration) as e:return dict(passed=False,reason='Catalog structure check failed: '+str(e))
        passed=True;reason='One-entry patch applies; native layout preserved.'
        if relevant:
            # Only changed entry destinations are checked; no claim of a full catalog scan.
            urls=folder/'urls.txt';urls.write_text('\n'.join(dict.fromkeys(relevant))+'\n')
            logs['changedEntryLinks']=run(['lychee','--no-progress','--verbose','--format','json','--max-retries','0','--max-concurrency','2','--timeout','10',str(urls)],folder,self.env)
            result=logs['changedEntryLinks']
            try:
                data=json.loads(result['stdout'])
                successful={r['url'].rstrip('/') for values in data.get('success_map',{}).values() for r in values}
                passed=result['exitCode']==0 and all(u.rstrip('/') in successful for u in relevant)
            except (ValueError,KeyError,TypeError):passed=False
            reason+=(' Changed-entry destinations verified.' if passed else ' Changed-entry links unverified/failed; held.')
        else:reason+=' Removal has no new destinations; factual removal evidence still requires maintainer review.'
        self.output.mkdir(parents=True,exist_ok=True)
        (self.output/('entry-'+proposal['id']+'.json')).write_text(json.dumps(logs,indent=2)+'\n')
        return dict(passed=passed,reason=reason,checks={k:v['exitCode'] for k,v in logs.items()},
                    scope='Patch applicability, one-entry structure and changed-entry URLs; no upstream lint suite exists in this snapshot.')
