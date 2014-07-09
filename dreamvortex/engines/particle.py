from dreamvortex.engines.engine import BaseItem, BaseEngine
from dreamvortex.vortex import Vortex
from dreamvortex.WavPlay import InitWavPlay, RandPlay
from dreamvortex import settings

from vroom.rendering.point_cloud import PointCloud

from random import random, randint


class Particle(BaseItem):
   
   def __init__(self, lifetime, vortex):
      BaseItem.__init__(self, lifetime, vortex)

#      c = settings.get_uniform('particle-color-range')
#      self.color = [c, 0.8, 0.3, 0.65]
      c = [settings.get_uniform('particle-red-range'), \
         settings.get_uniform('particle-green-range'), \
         settings.get_uniform('particle-blue-range'), \
         settings['particle-transparency']]
      self.color = c
      
   def step(self):
      self.vortex.step()

#   def draw(self):
#      self.buffer = PointCloud([x.vortex.pos for x in self.particles], \
#         [x.color for x in self.particles])
#      self.buffer.texture('data/particle.bmp')
#      self.buffer.pointSize(305.0)
#      self.buffer.draw(style='solid')

class ParticleEngine(BaseEngine):

   def __init__(self):
      BaseEngine.__init__(self)

   def add_particle(self):
      self.particles.append(Particle(randint(400, 600), Vortex.random_vortex()))

   def draw(self):
      if not len(self.particles):
         return 
      self.buffer = PointCloud([x.vortex.pos for x in self.particles], \
            [x.color for x in self.particles])
      self.buffer.sprite('data/particle.bmp')
      self.buffer.pointSize(300.0)
      self.buffer.draw()
#      for particle in self.buffer:
#         for particle in self.particles:
#            particle.texture.bind()
#            particle.draw()
#            particle.texture.unbind()

   def spawn(self):
      if random() < 0.06:      # originally 0.1
#         for _ in range(randint(1, 5)):
#            self.add_particle()
         self.add_particle()
         RandPlay()

