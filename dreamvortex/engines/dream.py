from dreamvortex.engines.engine import BaseParticle, BaseEngine
from dreamvortex.vortex import Vortex
from dreamvortex import settings, get_dream

from vroom.rendering.buffers import Buffer
from vroom.core.color import color, white

from random import random, randint


class DreamImage(BaseParticle):
   
   def __init__(self, lifetime):
      BaseParticle.__init__(self, lifetime, None)

      points, texcoords = Vortex.image_strip()
      self.dream = Buffer(points)
      self.dream.loadTexCoordData(texcoords)
      self.dream.renderMode('triangles:strip')

      self.texture = get_dream()

      self.color = [1.0, 1.0, 1.0, 0.0]

   def step(self):
      #self.vortex.step()
      if self.age < 150:
         self.color[3] += 1.0/150.0
      elif (self.lifetime - self.age) < 150:
         self.color[3] -= 1.0/150.0

   def draw(self):
      color(self.color)
      self.texture.bind()
      self.dream.draw(style='solid')
      self.texture.unbind()


class DreamEngine(BaseEngine):

   def __init__(self):
      BaseEngine.__init__(self)

   def add_particle(self):
      self.particles.append(DreamImage(randint(400, 800)))

   def draw(self):
      if not len(self.particles):
         return 

      for dream in self.particles:
         dream.draw()
         
   def spawn(self):
      if len(self.particles) < 15 and random() < 0.05:
         self.add_particle()

