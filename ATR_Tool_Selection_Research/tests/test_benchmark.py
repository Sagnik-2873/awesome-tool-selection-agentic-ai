import unittest
from src.benchmark import catalog,make_cases,validate
from src.selectors import Selector
from src.run_experiment import boot_ci
class BenchmarkTests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):cls.tools=catalog();cls.cases=make_cases()
 def test_01_unique_gold(self):self.assertTrue(validate(self.tools,self.cases))
 def test_02_counts(self):self.assertEqual(len(self.tools),96);self.assertGreater(len(self.cases),500)
 def test_03_no_tool(self):
  q=next(x['query'] for x in self.cases if x['condition']=='no_tool')
  self.assertIsNone(Selector(self.tools,'constraint_aware').select(q))
 def test_04_impossible_tool(self):
  q=next(x['query'] for x in self.cases if x['condition']=='no_valid')
  self.assertIsNone(Selector(self.tools,'constraint_aware').select(q))
 def test_05_valid_selection(self):
  c=next(x for x in self.cases if x['condition']=='valid')
  self.assertIn(Selector(self.tools,'constraint_aware').select(c['query']),c['gold_ids'])
 def test_06_determinism(self):
  c=self.cases[-1];model=Selector(self.tools,'tfidf_word');self.assertEqual(model.select(c['query']),model.select(c['query']))
 def test_07_perturbation_metadata(self):
  x=self.tools[0]
  for v in ('original','reordered','distractor'):
   self.assertIn(Selector(self.tools,'constraint_aware',v).select('Find weather forecasts for india with live information in json format.'),[x['id']])
 def test_08_bootstrap_zero(self):self.assertEqual(boot_ci([1,0,1],[1,0,1]),[0.,0.])
if __name__=='__main__':unittest.main()
