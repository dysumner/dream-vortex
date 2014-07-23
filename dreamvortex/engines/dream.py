from dreamvortex.engines.engine import BaseItem, BaseEngine
from dreamvortex.vortex import Vortex
from dreamvortex import settings, get_dream

from vroom.rendering.buffers import Buffer
from vroom.core.color import color, white

from random import random, randint, randrange


class DreamImage(BaseItem):
   
   def __init__(self, lifetime):
      BaseItem.__init__(self, lifetime, None)

      points, texcoords = Vortex.image_strip()
#      print len(points)
      delta_x = -points[6][0] + randrange(-10,10)   #- points[7][0]
      delta_y = -points[6][1] + randrange(-10,10)   #- points[7][1]
      delta_z = - points[0][2]   
      
      # Added to move dreams down in the space - messes up rendering w/ vortex
      for i in range(len(points)):
         points[i][0] = points[i][0] + delta_x
         points[i][1] = points[i][1] + delta_y
         points[i][2] = points[i][2] + delta_z
      
      self.dream = Buffer(points)
      self.dream.loadTexCoordData(texcoords)
      self.dream.renderMode('triangles:strip')

      self.texture = get_dream()

      self.color = [1.0, 1.0, 1.0, 0.0]
         
#      self.dream.move_to([0.,0.,0.])

   def step(self):
      #self.vortex.step()
      
      # The following lines fade in and out the dreams
      if self.age < 150:
         self.color[3] += 1.0/150.0
      elif (self.lifetime - self.age) < 150:
         self.color[3] -= 1.0/150.0
         
#      self.dream.move_to([0.,0.,0.])


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
      if len(self.particles) < 2 and random() < 0.01:
         self.add_particle()

