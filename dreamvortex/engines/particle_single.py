from dreamvortex.engines.base_item import BaseItem
from dreamvortex.vortex import Vortex
from dreamvortex.WavPlay import RandPlay
from dreamvortex import settings

from vroom.rendering.point_cloud import PointCloud

from random import randint, uniform


class Particle(BaseItem):
   
   def __init__(self):
      
      lifetime = randint(400, 600)  # 400, 600
      vortex = Vortex.random_vortex()
      
      BaseItem.__init__(self, lifetime, vortex)
      
      c = [settings.get_uniform('particle-red-range'), \
         settings.get_uniform('particle-green-range'), \
         settings.get_uniform('particle-blue-range'), \
         settings['particle-transparency']]
      self.color = c
      
      # set transform for z to be 1 above floor
      self.transforms[2] = 1.
      
      RandPlay()

   def step(self):
      self.vortex.step()
      self.age += 1

   def draw(self):
      self.buffer = PointCloud([self.vortex.pos],[self.color])
      self.buffer.sprite('data/particle.bmp')
      self.buffer.pointSize(200.0)
      self.buffer.draw()


