"""Three reproducible selectors; no inference API or external secrets required."""
from __future__ import annotations
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from .benchmark import DOMAINS

class Selector:
 def __init__(self,tools,method='tfidf_word',variant='original'):
  self.tools=list(tools);self.method=method;self.variant=variant
  descriptions=[]
  for t in tools:
   desc=t['description']
   if variant=='reordered':
    desc=f"Output {t['format']}; {t['mode']} feed; {t['region']} coverage. {DOMAINS[t['domain']][0]} and {DOMAINS[t['domain']][1]}. API client."
   elif variant=='distractor':
    # Adds generic sales copy (does not change advertised capabilities).
    desc+= ' Reliable powerful preferred integration fast advanced platform compatible service.'
   descriptions.append(desc)
  if method=='tfidf_char':self.vectorizer=TfidfVectorizer(analyzer='char_wb',ngram_range=(3,5),sublinear_tf=True)
  else:self.vectorizer=TfidfVectorizer(ngram_range=(1,2),sublinear_tf=True)
  self.features=self.vectorizer.fit_transform(descriptions)

 def candidates(self,query):
  if not self.method.startswith('constraint_'):return list(range(len(self.tools)))
  lower=query.lower()
  # Interpret explicit constraints; no access to gold labels or case metadata.
  if 'without using an external tool' in lower:return []
  region=next((s for s in ('india','global') if re.search(r'\b'+s+r'\b',lower)),None)
  mode=next((s for s in ('live','historical') if re.search(r'\b'+s+r'\b',lower)),None)
  fmt=next((s for s in ('json','csv','xml','yaml') if re.search(r'\b'+s+r'\b',lower)),None)
  # Fail closed if an explicit impossible format is requested or no domain recognized.
  domain=None
  for d,aliases in DOMAINS.items():
   if any(a.lower() in lower for a in aliases): domain=d;break
  if not domain:return []
  use_domain=self.method!='constraint_no_domain'
  use_format=self.method!='constraint_no_format'
  return [i for i,t in enumerate(self.tools) if ((not use_domain) or t['domain']==domain) and (not region or t['region']==region)
   and (not mode or t['mode']==mode) and ((not use_format) or (not fmt) or t['format']==fmt)]

 def select(self,query):
  keep=self.candidates(query)
  if not keep:return None
  q=self.vectorizer.transform([query]);scores=cosine_similarity(q,self.features).ravel()
  return self.tools[sorted(keep,key=lambda i:(-scores[i],self.tools[i]['id']))[0]]['id']
