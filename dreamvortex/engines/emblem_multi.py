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
   
   def __init__(self, emb=None, lifetime=randint(4000, 6000)):
      
      BaseItem.__init__(self, lifetime)

      if emb == None:
         emb = randint(1,emblem_data['number'])
      print 'emblem number = ', emb
      
      # True in the following line creates normals
      self.mesh = Mesh.from_ply(Global.filename[emb-1], True)
      print 'emblem mesh made'
      self.type = 'emblem'
      self.emb = emb       # Gives the emblem number to associate w/ dream
      
      # Set the material properties
      self.material = emblem_data[('color'+str(emb))]
      self.style = 'solid'
      self.transparency = False
      
      # Position and Scale the Emblem for the vortex
      # Position determined by reading info from a file (pre-measured)
      pos = emblem_data[('center'+str(emb))]
      self.mesh.move_to(pos)
      # try this for position since moved to the  origin
      self.pos = [0.,0.,0.]
        
      self.transforms = [[0.,0.,-1.],[0.,0.,0.],
            emblem_data[('scale'+str(emb))]]
            
      # Make the emblem selectable, but not moveable
            
      # define rate of rise
      self.z_step = 0.02    
      
      # Set dragging defaults
      self.dragging = False
      self.hover = False

   def draw(self):
      lighting(True)
      transparency(False)
      material(self.material)
      self.mesh.draw(style=self.style)
#      material([1.,1.,1.])
      lighting(False)      # to retain previous lighing setting

   def step(self): 
      self.transforms[0][2] += self.z_step # z transform
      self.transforms[1][2] += 0.5         # rotation around z-axis
      self.age += 1
      
      
