'''
3d mesh emblems
July, Djerassi, Sumner
'''

from dreamvortex.engines.base_item import BaseItem
from vroom import *
import vroom.extra.PLY

from dreamvortex import emblem_data, get_emblem

#from vroom.rendering.buffers import Buffer
#from vroom.core.color import color

from random import randint

class Emblem(BaseItem):

   lifetime = randint(4000, 6000)  
   
   def __init__(self, lifetime=randint(4000, 6000)):
      
      BaseItem.__init__(self, lifetime)


      # True in the following line creates normals
      self.mesh = Mesh.from_ply(Global.filename, True) 
      self.color = [1.0, 0.0, 0.0]
      self.material = self.color 
      self.style = 'solid'
      self.transforms = [0.,0.,-1.,0.,0.,0.,5.]
      
      self.mesh.move_to([-.17,-.47,-.67])
#      print 'origin', self.origin

   def draw(self):
      lighting(True)
      transparency(False)
      material(self.material)
      self.mesh.draw(style=self.style)
#      material([1.,1.,1.])
      lighting(False)      # to retain previous lighing setting

   def step(self): 
      self.transforms[2] += 0.02      # z transform
      self.transforms[5] += .5         # rotation around z-axis
      self.age += 1
      
      
