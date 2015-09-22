'''
functions for drawing comment environment elements for the dream vortex
Dawn Sumner, Djerassi, July 2014
'''

from vroom import *
from dreamvortex.general_utilities2 import invert
#from dreamvortex.engines.engine import BaseItem, BaseEngine

class Floor:

   def __init__(self, points, tex):
   
      # Make the floor
      coords = [[0.,0.],[1.,0.],[0.,1.],[1.,1.]]
      self.buffer = Buffer(points)
      self.buffer.loadTexCoordData(coords)
      self.buffer.renderMode('triangles:strip')
      
      # Set the drawing properties
      self.texture = tex
      self.transp = True     #transparency
      self.color = [1.,1.,1.,1.]
      
      # Locate it and make it fixed in space
      self.pos = invert(center(points))     # center is a vroom function 
      # RIGHT NOW CENTER RETURNS THE INVERSE CENTER SO NEED THE INVERT COMMAND
#      print points
#      print self.pos
      self.transforms = [[0.,0.,0.],[0.,0.,0.],1.0]
      self.moveable = False
      
   def draw(self):
   
      glDisable(GL_CULL_FACE)

      transparency(self.transp)
      color(self.color)
      self.texture.bind()             
      self.buffer.draw(style='solid') 
      self.texture.unbind()
      
   def step(self):
      if self.color[3] < 0.8:
         self.color[3] += .001
      else:
         pass


