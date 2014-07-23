from math import sin, cos, pi, sqrt, atan
from random import random, uniform, randint

from vroom.rendering.point_cloud import PointCloud
from vroom.rendering.buffers import Buffer
from vroom import color

from dreamvortex import settings
from dreamvortex.vortex import Vortex

class Particle:
   def __init__(self, lifetime, vortex):
      self.lifetime = lifetime
      self.vortex = vortex

      self.age = 0

      c = settings.get_uniform('particle-color-range')   #gives a random number btw min and max in file
      self.color = [c, 0.8, 0.3, 0.65]    #c gives the R value for RGBT

   @staticmethod
   def RandomParticle():
      return Particle(randint(400, 600), Vortex.random_vortex())

   def step(self):
      self.vortex.step()

   def expired(self):
      return self.age > self.lifetime

class ParticleTrail:
   def __init__(self, lifetime, vortex):
      self.lifetime = lifetime
      self.vortex = vortex

      self.points = []
      self.coords = []

      self.age = 0

      self.history = randint(15, 30)
      self.height = uniform(0.5, 3.25)

      c = random()
      self.color = [c, c, c, 0.4]

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

   def expired(self):
      return self.age > self.lifetime

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

   @staticmethod
   def RandomParticleTrail():
      return ParticleTrail(randint(400, 550), Vortex.random_vortex())

class EngineTrail:
   def __init__(self):
      self.particles = []

   def add_particle(self):
      self.particles.append(ParticleTrail.RandomParticleTrail())

   def step(self):
      for particle in self.particles:
         if particle.expired():
            self.particles.remove(particle)
            continue
         particle.step()
         particle.age += 1

      if random() < 0.05:
         for _ in range(randint(1, 5)):
            self.add_particle()

   def draw(self):
      for particle in self.particles:
         particle.draw()

class Engine:
   def __init__(self):
      self.particles = []

   def add_particle(self):
      self.particles.append(Particle.RandomParticle())

   def step(self):
      for particle in self.particles:
         if particle.expired():
            self.particles.remove(particle)
            continue
         particle.step()
         particle.age += 1

      if random() < 0.05:     # originally 0.1; want to change this to a setting
         for _ in range(randint(1, 5)):
            self.add_particle()

   def draw(self):
      if not len(self.particles):
         return 
      self.buffer = PointCloud([x.vortex.pos for x in self.particles], [x.color for x in self.particles])
      self.buffer.sprite('data/particle.bmp')
      self.buffer.pointSize(105.0)
      self.buffer.draw()

