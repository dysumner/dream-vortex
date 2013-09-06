import yaml
import random

class Settings:

   def __init__(self, filename):
      self.doc = yaml.load(open(filename))

      for key, val in self.doc.items():
         setattr(self, key, val)

   def __getitem__(self, key):
      return self.doc[key]

   def get_uniform(self, key):
      return random.uniform(self.doc[key]['min'], self.doc[key]['max'])
