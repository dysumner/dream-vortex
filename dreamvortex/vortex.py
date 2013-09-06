from random import random
from math import sin, cos, pi
from dreamvortex import settings

def vortex_generator(steps, a, b):
   theta = random()*2.0*pi
   beta = 0.1
   for t in steps:
      r = a + b * theta
      x = r * cos(theta)
      y = r * sin(theta)
      yield [x, y, t]
      theta += beta

def random_vortex(steps, step_size):
   steps = [i*step_size for i in range(steps)]
   a = settings.get_uniform('a')
   b = settings.get_uniform('b')
   return list(vortex_generator(steps, a, b))
