'''Dreams for scene 2 of the dream vortex
Dawn Sumner, Djerassi, July 2014, based on Jordan's dream.py
'''

from dreamvortex.engines.base_item import BaseItem
from dreamvortex.vortex import Vortex
from dreamvortex import settings, get_dream
from dreamvortex.general_utilities import distance

from vroom.rendering.buffers import Buffer
from vroom import *

from random import random, randint, randrange


class DreamImage(BaseItem):
   
   def __init__(self,dream_number=None):
   
      lifetime = 10000
      BaseItem.__init__(self, lifetime, None)

      points, texcoords = Vortex.dream_image()
      
      self.dream = Buffer(points)
      self.dream.loadTexCoordData(texcoords)
      self.dream.renderMode('triangles:strip')

      self.texture = get_dream(dream_number)
      self.color = [1.0, 1.0, 1.0, .0]
      
      # move the dreams around
      print points[0]
      
      delta_x = 0
      delta_y = 0
      
      if distance(points[0],[0,0,0]) < 5.:
         delta_x = points[0][0]
         delta_y = points[0][1]
      if distance(points[0],[0,0,0]) > 20:
         delta_x = -points[0][0]/2.
         delta_y = -points[0][1]/2.
         
      delta_z = 8.   

      self.transforms = [delta_x,delta_y,delta_z,0.,0.,0.,1.0]
         
   def step(self):
      
      # The following lines fade in and out the dreams
      if self.age < 1000 and self.color[3] < 1:
         self.color[3] += 1.0/1000.0
#      elif (self.lifetime - self.age) < 150:
#         self.color[3] -= 1.0/150.0
         
      self.age += 1

   def draw(self):
      transparency(True)
      lighting(False)
      color(self.color)
      self.texture.bind()
      
      glDisable(GL_CULL_FACE)

      self.dream.draw(style='solid')
      self.texture.unbind()

