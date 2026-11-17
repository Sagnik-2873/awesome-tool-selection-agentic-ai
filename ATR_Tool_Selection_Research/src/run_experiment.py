"""Compute predictions, metrics, paired uncertainty and publication figures."""
from __future__ import annotations
import csv,json,time,platform,random,sys,hashlib
from pathlib import Path
from collections import defaultdict
import numpy as np
from .benchmark import write_data
from .selectors import Selector
ROOT=Path(__file__).resolve().parents[1]
METHODS=['tfidf_word','tfidf_char','constraint_aware','constraint_no_domain','constraint_no_format']
VARIANTS=['original','reordered','distractor']

def boot_ci(a,b,seed=2026,repeats=3000):
 # Pairwise bootstrap over case IDs: delta of valid top1 (method A minus B).
 assert len(a)==len(b)
 n=len(a);rng=np.random.default_rng(seed);d=np.asarray(a,dtype=float)-np.asarray(b,dtype=float)
 sample=rng.integers(0,n,size=(repeats,n));means=d[sample].mean(axis=1)
 return [float(np.quantile(means,.025)),float(np.quantile(means,.975))]

def run(root=ROOT):
 root=Path(root); t,c=write_data(root/'dataset'); res=root/'results';res.mkdir(exist_ok=True)
 records=[]
 for variant in VARIANTS:
  for method in METHODS:
   model=Selector(t,method,variant)
   for case in c:
    start=time.perf_counter_ns();p=model.select(case['query']);elapsed=(time.perf_counter_ns()-start)/1e6
    valid=int((p in case['gold_ids']) if case['gold_ids'] else p is None)
    records.append({'case_id':case['id'],'split':case['split'],'condition':case['condition'],
     'variant':variant,'method':method,'prediction':p or 'ABSTAIN',
     'gold':','.join(case['gold_ids']) or 'ABSTAIN','correct':valid,'latency_ms':round(elapsed,6)})
 fieldnames=list(records[0]);
 with (res/'predictions.csv').open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=fieldnames);w.writeheader();w.writerows(records)
 stats=[]
 for split in ('train','dev','test'):
  for variant in VARIANTS:
   for method in METHODS:
    sub=[r for r in records if r['split']==split and r['variant']==variant and r['method']==method]
    for condition in ('all','valid','no_valid','no_tool'):
     ss=sub if condition=='all' else [x for x in sub if x['condition']==condition]
     if not ss:continue
     stats.append({'split':split,'variant':variant,'method':method,'condition':condition,'n':len(ss),'correct':sum(x['correct'] for x in ss),
       'accuracy':round(sum(x['correct'] for x in ss)/len(ss),6),'mean_latency_ms':round(float(np.mean([x['latency_ms'] for x in ss])),4)})
 with (res/'metrics.csv').open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=list(stats[0]));w.writeheader();w.writerows(stats)
 ci=[]
 for variant in VARIANTS:
  group={m:{r['case_id']:r['correct'] for r in records if r['split']=='test' and r['variant']==variant and r['method']==m} for m in METHODS}
  ids=sorted(group['tfidf_word'])
  for other in METHODS[1:]:
   a=[group[other][k] for k in ids];b=[group['tfidf_word'][k] for k in ids]
   low,high=boot_ci(a,b)
   ci.append({'variant':variant,'comparison':other+' minus tfidf_word','n':len(ids),'delta':round(float(np.mean(a)-np.mean(b)),6),'lower95':round(low,6),'upper95':round(high,6)})
 with (res/'paired_bootstrap.csv').open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=list(ci[0]));w.writeheader();w.writerows(ci)
 fingerprints={k:hashlib.sha256((root/k).read_bytes()).hexdigest() for k in ['dataset/cases.json','dataset/tools.json']}
 env={'python':platform.python_version(),'numpy':np.__version__,'scikit_learn':__import__('sklearn').__version__,'methods':METHODS,'variants':VARIANTS,
  'seed':2026,'bootstrap_replicates':3000,'tool_count':len(t),'case_count':len(c),'sha256':fingerprints}
 (res/'environment.json').write_text(json.dumps(env,indent=2)+'\n')
 return stats,ci
if __name__=='__main__':
 stats,ci=run();print('TEST ORIGINAL');print(*[s for s in stats if s['split']=='test' and s['variant']=='original' and s['condition']=='all'],sep='\n');print('CIs',ci)
