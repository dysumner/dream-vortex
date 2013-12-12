from dreamvortex.engines.engine import BaseParticle, BaseEngine
from dreamvortex.vortex import Vortex
from dreamvortex import settings

from vroom.rendering.point_cloud import PointCloud

from random import random, randint


class Particle(BaseParticle):
   
   def __init__(self, lifetime, vortex):
      BaseParticle.__init__(self, lifetime, vortex)

      c = settings.get_uniform('particle-color-range')
      self.color = [c, 0.8, 0.3, 0.65]

   def step(self):
      self.vortex.step()


class ParticleEngine(BaseEngine):

   def __init__(self):
      BaseEngine.__init__(self)

   def add_particle(self):
      self.particles.append(Particle(randint(400, 600), Vortex.random_vortex()))

   def draw(self):
      if not len(self.particles):
         return 
      self.buffer = PointCloud([x.vortex.pos for x in self.particles], [x.color for x in self.particles])
      self.buffer.sprite('data/particle.bmp')
      self.buffer.pointSize(105.0)
      self.buffer.draw()

   def spawn(self):
      if random() < 0.1:
         for _ in range(randint(1, 5)):
            self.add_particle()
