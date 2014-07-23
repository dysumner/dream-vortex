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

class ParticleEngine(BaseEngine):

   def __init__(self):
      BaseEngine.__init__(self)

   def add_particle(self):
      self.particles.append(Particle(randint(400, 600),
            Vortex.random_vortex()))
            
      # for new class
      self.transforms = [0.,0.,-3.,0.,0.,0.,1.0]

   def draw(self):
      if not len(self.particles):
         return 
      self.buffer = PointCloud([x.vortex.pos for x in self.particles],
            [x.color for x in self.particles])
      self.buffer.sprite('data/particle.bmp')
      self.buffer.pointSize(300.0)
      self.buffer.draw()

   def spawn(self):
      if random() < 0.06:     
         self.add_particle()
         RandPlay()

