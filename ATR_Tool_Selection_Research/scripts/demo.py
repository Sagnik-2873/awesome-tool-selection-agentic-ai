"""Display a reproducible, local comparison for one tool selection request."""
import argparse
from src.benchmark import catalog
from src.selectors import Selector

EXAMPLE='Find weather forecasts for india with live information in json format.'

def main():
 parser=argparse.ArgumentParser(description='Inspect local tool choices; no external API requests')
 parser.add_argument('--query',default=EXAMPLE,help='Natural-language tool-selection request')
 args=parser.parse_args()
 print('Request:',args.query)
 for method in ('tfidf_word','tfidf_char','constraint_aware','constraint_no_domain','constraint_no_format'):
  prediction=Selector(catalog(),method).select(args.query)
  print(f'{method:22s} {prediction or "ABSTAIN"}')

if __name__=='__main__':main()
