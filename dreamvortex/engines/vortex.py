from dreamvortex.engines.engine import BaseParticle, BaseEngine
from dreamvortex.vortex import Vortex
from dreamvortex import settings, get_strip

from vroom.rendering.buffers import Buffer
from vroom.core.color import color

from random import random, randint, uniform
from math import sin, cos


class BrushStroke(BaseParticle):
   
   def __init__(self, lifetime, vortex):
      BaseParticle.__init__(self, lifetime, vortex)

      self.points = []
      self.coords = []

      self.history = randint(15, 30)
      self.height = uniform(0.5, 3.25)

      c = random()
#      c = [0.2,0.2,0.2]
      self.color = [c, c, c, 1.0]   # gives the strips various intensities
      
      # To put a random dream on the strip
      self.texture = get_strip()

      self.initialize()
      self.step()

   def initialize(self):
      r = self.vortex.a + self.vortex.b * self.vortex.theta
      x = r * cos(self.vortex.theta)
      y = r * sin(self.vortex.theta)

      x = 0.0
      dx = 1.0 / self.history

      for _ in range(self.history):
         self.points.append([x, y, -self.height])
         self.points.append([x, y,  self.height])

         self.coords.append([x, 0.0])
         self.coords.append([x, 1.0])
         x += dx

      self.points.append([x, y, -self.height])
      self.points.append([x, y,  self.height])

      self.coords.append([1.0, 0.0])
      self.coords.append([1.0, 1.0])

   def step(self):
      x,y,z = self.vortex.step()

      self.points.append([x, y, z-self.height])
      self.points.append([x, y, z+self.height])
      self.points.pop(0)
      self.points.pop(0)

      self.buffer = Buffer(self.points)
      self.buffer.loadTexCoordData(self.coords)
      self.buffer.renderMode('triangles:strip')

   def draw(self):
      if self.age < self.history:
         return
      color(self.color)
      self.buffer.draw(style='solid')

class VortexEngine(BaseEngine):

   def __init(self):
      BaseEngine.__init__(self)

      self.particles = []
      
   def add_particle(self):
      self.particles.append(BrushStroke(randint(400, 500), Vortex.random_vortex()))
      self.texture = get_strip()    # added to put dream images on strips

   def draw(self):
      for particle in self.particles:
         particle.texture.bind()
         particle.draw()
         particle.texture.unbind()

   def spawn(self):
      if random() < 0.02:    # originally 0.05
         for _ in range(randint(1, 5)):
            self.add_particle()


