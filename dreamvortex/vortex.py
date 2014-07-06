from random import random, uniform, randint
from math import sin, cos, pi, degrees
from dreamvortex import settings

class Vortex:
   ''' The vortex dynamics are uniquely defined by the following parameters:
          a -- spiral parameter  = radius equiavlent at theta = 0
          b -- spiral parameter  = expansion of spirals
          theta_step -- rotational step size
          z_step -- vertical step size

       The Vortex class encapsulates this data and additionally stores a current
       position (angle and position).
   '''

   @staticmethod
   def radius(a, b, theta):
      ''' Compute radius for given angle and spiral parameter values.'''
      return a + b * theta


   def __init__(self, a, b, r_step, z_step):
      # Set vortex parameters
      self.a, self.b = a, b # spiral parameters
      self.r_step = r_step  # rotational step size
      self.z_step = z_step  # vertical step size

      # Initialize current possition
      # We begin with a random angle and a height of zero - dys changed to -10
      self.theta = random()*2.0*pi 
      r = Vortex.radius(self.a, self.b, self.theta)
      self.pos = [r*cos(self.theta), r*sin(self.theta), settings['z-offset']]
   
   def __str__(self):
      return '(vortex a={}, b={}, dr={}, dz={})'.format(self.a, self.b, self.r_step, self.z_step)

   def step(self):
      ''' Update current position to the next point along the vortex path.

      returns -- new current position (x,y,z).
      '''
      # Increment the current angle and compute the new radius
      self.theta += self.r_step
      radius = Vortex.radius(self.a, self.b, self.theta)

      # Update position and return value
      x = radius * cos(self.theta)
      y = radius * sin(self.theta)
      z = self.pos[2] + self.z_step
      self.pos = [x,y,z]
      return self.pos


   # Static generators and initializaton functions
   #

   @staticmethod
   def random_vortex():
      a = settings.get_uniform('a')
      b = settings.get_uniform('b')
#      dr = settings['delta-theta']
      dr = settings['delta-theta'] * (1.5/(a*a+b*b)**0.5)
#      dz = settings['delta-z']
      dz = settings['delta-z'] * (1./(a*a+b*b)**0.5)
      return Vortex(a, b, dr, dz)

   @staticmethod
   def line_generator(steps, vortex):
      for _ in range(steps):
         yield vortex.step()

   @staticmethod
   def random_path(steps):
      return list(Vortex.line_generator(steps, Vortex.random_vortex()))

   @staticmethod
   def strip_generator(steps, vortex, height):
      #height = settings.get_uniform('height')

      # randomize start point
      for _ in range(randint(0, 300)):
         vortex.step()

      for _ in range(steps):
         (x,y,z) = vortex.step()
         yield [x,y,z-height]
         yield [x,y,z+height]

   @staticmethod
   def image_generator(steps, vortex, height):
      #height = settings.get_uniform('height')

      for _ in range(steps):
         (x,y,z) = vortex.step()
         yield [x,y,z-height]
         yield [x,y,z+height]
   
      (x,y,z) = vortex.step()
      yield [x,y,z-height]
      yield [x,y,z+height]
   
   
   @staticmethod
   def texcoord_generator(steps):
      dx = 1.0/(steps/2.0)
      x = 0.0
      for i in range((steps-1)/2):
         yield (x, 0.0)
         yield (x, 1.0)
         x += dx 
      yield (1.0, 0.0)
      yield (1.0, 1.0)

   @staticmethod
   def random_strip(steps):
      vortex = Vortex.random_vortex()
      height = settings.get_uniform('height')
      points = list(Vortex.strip_generator(steps, vortex, height))
      coords = list(Vortex.texcoord_generator(len(points)))
      return points, coords

   @staticmethod
   def image_strip():
      vortex = Vortex.random_vortex()

      # randomize start point
      for _ in range(randint(100, 450)):
         vortex.step()

      steps = 6
      d_theta = steps*vortex.r_step

      r1 = Vortex.radius(vortex.a, vortex.b, vortex.theta)
      r2 = Vortex.radius(vortex.a, vortex.b, (vortex.theta+d_theta))
      ravg = (r1 + r2) / 2.0

      s1 = r1 * d_theta
      s2 = r2 * d_theta
      savg = ravg * d_theta

      height = savg / 2.0

      points = list(Vortex.image_generator(steps, vortex, height))
      coords = list(Vortex.texcoord_generator(len(points)))
      return points, coords 
