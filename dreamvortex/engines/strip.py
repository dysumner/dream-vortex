from dreamvortex.engines.engine import BaseItem, BaseEngine
from dreamvortex.vortex import Vortex
from dreamvortex import settings, get_strip

from vroom.rendering.buffers import Buffer
from vroom.core.color import color

from random import random, randint, uniform
from math import sin, cos


class Strip(BaseItem):
   
   def __init__(self, lifetime, vortex):
      BaseItem.__init__(self, lifetime, vortex)

      self.points = []
      self.coords = []

      self.history = randint(15, 30)
      self.height = uniform(0.5, 3.25)
      
      c = uniform(0.000001, 0.8)
#      c = [0.2,0.2,0.2]
      self.color = [c, c, c, 1.0]   # gives the strips various intensities
      
      # Puts a random dream on the strip
      self.texture = get_strip()

      self.initialize()
      self.step()     # This step() results in self.buffer() being defined

   def initialize(self):

      x_tex = 0.0                                  #orig x
      dx = 1.0 / self.history
      theta_step = settings['delta-theta']         #added
      
      # z_b, z_t used to place the strip below the floor & have it emerge
      z_step = self.vortex.z_step
      z_b = -2*self.height - (self.history * z_step)
      z_t = -self.history * z_step

      for _ in range(self.history):
         r = self.vortex.a + self.vortex.b * self.vortex.theta #added
         x = r * cos(self.vortex.theta)                        #added
         y = r * sin(self.vortex.theta)                        #added
         
         self.points.append([x, y, z_b])             #orig z = -self.height
         self.points.append([x, y, z_t])             #orig z = self.height

         self.coords.append([x_tex, 0.0])          #orig used x
         self.coords.append([x_tex, 1.0])
         
         x_tex += dx
         self.vortex.theta += theta_step           #added
         z_b += z_step
         z_t += z_step

      self.points.append([x, y, z_b])              #orig z = -self.height
      self.points.append([x, y, z_t])              #orig z = self.height

      self.coords.append([1.0, 0.0])
      self.coords.append([1.0, 1.0])
      
      self.vortex.pos[2] = - self.height
#      print self.points[0], self.points[1]

   def step(self):
      x,y,z = self.vortex.step()

      self.points.append([x, y, z-self.height])
      self.points.append([x, y, z+self.height])
      self.points.pop(0)
      self.points.pop(0)   # need pop twice (empirically)

      self.buffer = Buffer(self.points)
      self.buffer.loadTexCoordData(self.coords)
      self.buffer.renderMode('triangles:strip')

   def draw(self):
         
      color(self.color)
      self.buffer.draw(style='solid')

class StripEngine(BaseEngine):

   def __init(self):
      BaseEngine.__init__(self)

      self.particles = []
      
   def add_particle(self):
      self.particles.append(Strip(randint(400, 500), Vortex.random_vortex()))

   def draw(self):
      for particle in self.particles:
#         print particle.texture
         particle.texture.bind()
         particle.draw()
         particle.texture.unbind()

   def spawn(self):
      if random() < 0.07:    
         self.add_particle()


