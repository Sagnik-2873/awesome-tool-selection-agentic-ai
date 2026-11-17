"""Deterministic, self-contained structured API tool-selection benchmark.

Cases are independently generated from task specifications; tool features are public.
This dataset is illustrative and synthetic, not a real-user or published benchmark.
"""
from __future__ import annotations
import json,random,re
from pathlib import Path

DOMAINS={
 'weather':('meteorological forecasts','weather forecasts','weather report','temperature and rain','climate outlook'),
 'currency':('foreign exchange rates','currency exchange','money conversion rates','forex quotes','exchange values'),
 'maps':('route navigation','map directions','driving routes','travel navigation','road directions'),
 'news':('news headlines','news articles','current events','press headlines','media updates'),
 'translation':('language translation','translate text','language conversion','translate sentences','multilingual translations'),
 'stocks':('equity market prices','stock prices','share price quotes','equities trading quotes','stock market data'),
 'sports':('sports results','sports scores','match outcomes','game results','sports fixtures'),
 'flights':('air travel status','flight status','airline tracking','flight movements','flight delays'),
 'traffic':('road traffic conditions','traffic congestion','highway delays','road congestion','commute traffic'),
 'hotels':('hotel room availability','hotel bookings','lodging availability','room vacancy','accommodation listings'),
 'shopping':('retail product catalog','product shopping','item listings','consumer goods','online merchandise'),
 'health':('medical facility directory','find clinics','hospital listings','clinic search','medical centers'),
}
REGIONS=('india','global'); MODES=('live','historical'); FORMATS=('json','csv')
# Case templates are held out by language family to expose lexical sensitivity.
TEMPLATES={
 'train': [
  'Find {alias} for {region} with {mode} information in {fmt} format.',
  'I need {region} {alias}; only {mode} data, {fmt} output.',
 ],
 'dev': [
  'Looking for a {fmt} endpoint supplying {alias}, area {region}, timing {mode}.',
 ],
 'test': [
  'Please select a service: {alias}. Coverage must be {region}; data must be {mode}; return {fmt}.',
  'For my application, use {alias} in {fmt}, restricted to {region} and {mode} mode.',
 ]
}

def catalog():
 tools=[]
 for domain,aliases in DOMAINS.items():
  for region in REGIONS:
   for mode in MODES:
    for fmt in FORMATS:
     tools.append({'id':f'{domain}__{region}__{mode}__{fmt}', 'domain':domain,'region':region,
       'mode':mode,'format':fmt,
       'description':f'{aliases[0]} and {aliases[1]}. Data coverage {region}; {mode} feed. Supports {fmt} output. API client.'})
 return tools

def make_cases():
 cases=[]
 for split,templates in TEMPLATES.items():
  for domain,aliases in DOMAINS.items():
   alias=aliases[2] if split=='train' else aliases[3] if split=='dev' else aliases[4]
   for region in REGIONS:
    for mode in MODES:
     for fmt in FORMATS:
      for i,template in enumerate(templates):
       q=template.format(alias=alias,region=region,mode=mode,fmt=fmt)
       cases.append({'id':f'{split}-{domain}-{region}-{mode}-{fmt}-{i}','split':split,'condition':'valid',
                    'domain':domain,'region':region,'mode':mode,'format':fmt,'query':q,
                    'gold_ids':[f'{domain}__{region}__{mode}__{fmt}']})
   # impossible format requests; one for each domain in dev/test, varying mode/region
   if split in ('dev','test'):
    for i,fmt in enumerate(('xml','yaml')):
     q=f'Select a {fmt} service for {aliases[3]} in india with live updates.'
     cases.append({'id':f'{split}-{domain}-invalid-{fmt}','split':split,'condition':'no_valid',
      'domain':domain,'region':'india','mode':'live','format':fmt,'query':q,'gold_ids':[]})
   # user does not require external tool for these definition requests
   if split=='test':
    cases.append({'id':f'{split}-{domain}-no_tool','split':split,'condition':'no_tool',
      'domain':domain,'region':None,'mode':None,'format':None,
      'query':f'Explain what {aliases[1]} means without using an external tool.', 'gold_ids':[]})
 return cases

def validate(tools,cases):
 ids=[t['id'] for t in tools];assert len(ids)==len(set(ids))
 case_ids=[x['id'] for x in cases]; assert len(set(case_ids))==len(case_ids)
 for c in cases:
  actual=[t['id'] for t in tools if c['condition']=='valid' and all(t[k]==c[k] for k in ('domain','region','mode','format'))]
  assert sorted(actual)==sorted(c['gold_ids']),c['id']
  assert set(c['gold_ids']).issubset(set(ids))
 return True

def write_data(out):
 out=Path(out);out.mkdir(parents=True,exist_ok=True)
 tools=catalog();cases=make_cases();validate(tools,cases)
 (out/'tools.json').write_text(json.dumps(tools,indent=2)+'\n')
 (out/'cases.json').write_text(json.dumps(cases,indent=2)+'\n')
 return tools,cases

if __name__=='__main__':
 t,c=write_data(Path(__file__).resolve().parents[1]/'dataset');print('tools',len(t),'cases',len(c))
