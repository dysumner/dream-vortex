from dreamvortex.engines.base_item import BaseItem
from dreamvortex.vortex import Vortex
from dreamvortex import settings, get_strip, get_dancer

from vroom.rendering.buffers import Buffer
from vroom.core.color import color
from vroom import *

from random import random, randint, uniform
from math import sin, cos

class Strip(BaseItem):
   
   def __init__(self):
      
      lifetime = randint(300, 400)
      vortex = Vortex.random_vortex()
      
      BaseItem.__init__(self, lifetime, vortex)

      self.points = []
      self.coords = []

      self.history = randint(15, 30)
      self.height = uniform(0.5, 3.25)
 
      c = uniform(0.0005, 0.8)   # 0.0001 to 0.8 for vortex
      self.color = [c, c, c, 1.0]   # gives the strips various intensities
            
      # Initializes the texture (for donna's as well)
      try:
         self.texture = get_strip()
      except:
         self.texture = get_dancer()
         
      self.initialize()
      self.step()     # This step() results in self.buffer() being defined
      
      self.transforms = [[0.,0.,0.],[0.,0.,0.],1.]
      self.pos = [0.,0.,0.]

   def initialize(self):

      x_tex = 0.0                            # used for texture mapping
      dx = 1.0 / self.history                # incremental step between texture coords
      theta_step = settings['delta-theta']   # incremental step in angle
      
      # reassign z-value to below the floor
      z_step = self.vortex.z_step
      self.vortex.pos[2] = -self.height
            
      # z_b, z_t describe the bottom and top of the strip, respectively
      z_b = self.vortex.pos[2] - self.height - ((self.history+1) * z_step)
      z_t = self.vortex.pos[2] + self.height - ((self.history+1) * z_step)

      for i in range(self.history+1):
         r = self.vortex.a + self.vortex.b * self.vortex.theta # radius
         x = r * cos(self.vortex.theta)                        # x-position
         y = r * sin(self.vortex.theta)                        # y-position
         
         self.points.append([x, y, z_b])     # append location of strip points
         self.points.append([x, y, z_t])

         self.coords.append([x_tex, 0.0])    # append texture coordinates
         self.coords.append([x_tex, 1.0])
         
         x_tex += dx                         # increment texture coordinate
         self.vortex.theta += theta_step     # increment vortex angle
         z_b += z_step                       # increment vertical position
         z_t += z_step
         
   def step(self):
      x,y,z = self.vortex.step()
      
      self.points.append([x, y, z-self.height])
      self.points.append([x, y, z+self.height])
      self.points.pop(0)
      self.points.pop(0)   # need pop twice to remove the last two points

      self.buffer = Buffer(self.points)
      self.buffer.loadTexCoordData(self.coords)
      self.buffer.renderMode('triangles:strip')
      
      self.age += 1

   def draw(self):
      transparency(True)      # should be True for vortex

      glBlendFunc(GL_SRC_ALPHA, GL_ONE); 

      # the following 3 lines are necessary to get backs drawn on strips
      glDepthMask(GL_FALSE)     
      glDisable(GL_CULL_FACE)
      glCullFace(GL_BACK)
      
      self.texture.bind()
      color(self.color)
      self.buffer.draw(style='solid')
      self.texture.unbind()


