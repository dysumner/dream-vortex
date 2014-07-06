class BaseItem:      #changed name from BaseParticle to BaseItem

   def __init__(self, lifetime, vortex):
      self.lifetime = lifetime
      self.vortex = vortex

      self.age = 0

   def expired(self):
      return self.age > self.lifetime

   def step(self):
      raise NotImplementedError()


class BaseEngine:

   def __init__(self):
      self.particles = []

   def step(self):
      for particle in self.particles:
         if particle.expired():
            self.particles.remove(particle)
            continue
         particle.step()
         particle.age += 1

      self.spawn()

   def draw(self):
      raise NotImplementedError()

   def spawn(self):
      raise NotImplementedError()


