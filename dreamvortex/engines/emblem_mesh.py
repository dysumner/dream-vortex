'''
3d mesh emblems
July, Djerassi, Sumner
'''

from dreamvortex.engines.engine import BaseItem, BaseEngine
from vroom import *
import vroom.extra.PLY

# These are from emblem_flat.py
from dreamvortex.vortex import Vortex
from dreamvortex import settings, get_emblem, get_strip

from vroom.rendering.buffers import Buffer
from vroom.core.color import color

from random import random, randint, uniform
from math import sin, cos


class Emblem(BaseItem):
   
   def __init__(self, lifetime, vortex):
      filename = get_resource('emblems/shoe.ply')

      #originally False; True gives reflections
      self.mesh = Mesh.from_ply(filename, True) 
      self.color = [1.0, 0.0, 0.0] 
      self.style = 'solid'

class EmblemEngine(BaseEngine):

   def __init(self):
      BaseEngine.__init__(self)

      self.particles = []
      
   def add_particle(self):
      self.particles.append(Emblem(randint(2000, 3000)))

   def draw(self):
      lighting(True)
      
      for particle in self.particles:
         particle.draw(style=self.style)
         
      lighting(False)

   def spawn(self):
      if random() < 0.001:    
         self.add_particle()


