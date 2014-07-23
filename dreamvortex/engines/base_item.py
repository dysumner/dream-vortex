'''
Required items for basic graphic objects
Dawn Sumner, Djerassi, July 2014
'''

class BaseItem:

   def __init__(self, lifetime=1, vortex=None):
      self.lifetime = lifetime
      self.vortex = vortex
      self.age = 0
      self.transforms = [0.,0.,0.,0.,0.,0.,1.0]

   def expired(self):
      return self.age > self.lifetime

   def step(self):
      pass
      
   def draw(self):
      raise NotImplementedError()


