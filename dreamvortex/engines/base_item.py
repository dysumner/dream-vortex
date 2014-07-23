'''
Required items for basic graphic objects
Dawn Sumner, Djerassi, July 2014
'''

class BaseItem:
   '''Provides a superclass for dream vortex objects, including lifetime, 
   dynamics (if calculated by vortex), age and translations/rotations/scale.  
   BaseItem also provides a step method (pass) and raises an exception if the
   draw method is not defined in the subclass.  A method is provided to remove
   objects if their age > lifetime or if they are > 2 below the floor.
   '''
   def __init__(self, lifetime=1, vortex=None):
      self.lifetime = lifetime
      self.vortex = vortex
      self.age = 0
      self.transforms = [0.,0.,0.,0.,0.,0.,1.0]

   def expired(self):
      exp = False
      try:
         if self.transforms[2] < -2.:
            exp = True
            print 'too low'
      except: pass
      
      if self.age > self.lifetime:
         exp = True
#         print 'too old', self.age, '>', self.lifetime
         
      return exp

   def step(self):
      pass
      
   def draw(self):
      raise NotImplementedError()


