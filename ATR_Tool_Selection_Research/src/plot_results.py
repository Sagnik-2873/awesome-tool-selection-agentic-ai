"""Produce reproducible plots from saved metric CSVs."""
import csv
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[1]

def plot():
 metrics=list(csv.DictReader((ROOT/'results/metrics.csv').open()))
 labels=['Word TF-IDF','Character TF-IDF','Constraint-aware']
 keys=['tfidf_word','tfidf_char','constraint_aware']
 variant=['original','reordered','distractor']
 fig,ax=plt.subplots(figsize=(9,4.8));x=np.arange(len(labels));w=.23
 for i,v in enumerate(variant):
  vals=[float(next(z['accuracy'] for z in metrics if z['split']=='test' and z['method']==k and z['condition']=='all' and z['variant']==v)) for k in keys]
  ax.bar(x+(i-1)*w,[100*a for a in vals],w,label=v.capitalize())
 ax.set_xticks(x,labels);ax.set_ylabel('Valid top-1 accuracy (%)');ax.set_ylim(0,108);ax.legend(ncol=3,loc='upper left');ax.set_title('Held-out template test (228 synthetic cases)');ax.grid(axis='y',alpha=.2)
 fig.tight_layout();fig.savefig(ROOT/'figures/accuracy.png',dpi=200);plt.close(fig)
 fig,ax=plt.subplots(figsize=(9,4.6)); conditions=['valid','no_valid','no_tool'];x=np.arange(3)
 for i,k in enumerate(keys):
  vals=[float(next(z['accuracy'] for z in metrics if z['split']=='test' and z['variant']=='original' and z['condition']==c and z['method']==k)) for c in conditions]
  ax.bar(x+(i-1)*w,[100*a for a in vals],w,label=labels[i])
 ax.set_xticks(x,['Valid tool (n=192)','No feasible tool (n=24)','No tool needed (n=12)']);ax.set_ylabel('Correct decision (%)');ax.set_ylim(0,108);ax.legend(loc='upper right');ax.grid(axis='y',alpha=.2);ax.set_title('Performance by decision type (original descriptions)')
 fig.tight_layout();fig.savefig(ROOT/'figures/error_categories.png',dpi=200);plt.close(fig)
if __name__=='__main__':plot()
