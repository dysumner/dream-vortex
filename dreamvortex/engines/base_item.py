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
      
      # position of object center with respect to its own coordinate system 
      #     prior to object-specific transformations relative to other objects and
      #     prior to transformations to scale/orient for Vrui navigation environ
      if self.vortex:                     # True if self.vortex <> None
         # mutable object assignment, so don't update self.pos
         self.pos = self.vortex.pos 
      else:
         self.pos = None      
      
      # transformations to put the object in the correct place relative to other objects
      #     transforms[0] = x, y, z translations, respectively
      #     transforms[1] = rotations around x, y, z axes, respectively
      #     transforms[2] = scale
      self.transforms = None
      self.moveable = False      # make the default that the object can not be dragged  
      self.type = 'base'         # field to record object type    
      
   def expired(self):
      exp = False
      
      if self.transforms:                 # True if self.transforms <> None
         if self.transforms[0][2] < -4.:
            exp = True
            print 'too low'
      
      if self.age > self.lifetime:
         exp = True
#         print 'too old', self.age, '>', self.lifetime
         
      return exp

   def step(self):
      pass
      
   def draw(self):
      raise NotImplementedError()


