'''
functions for drawing comment environment elements for the dream vortex
Dawn Sumner, Djerassi, July 2014
'''

from vroom import *
#from dreamvortex.engines.engine import BaseItem, BaseEngine

class Floor:

   def __init__(self, points, tex):
      coords = [[0.,0.],[1.,0.],[0.,1.],[1.,1.]]
      self.buffer = Buffer(points)
      self.buffer.loadTexCoordData(coords)
      self.buffer.renderMode('triangles:strip')
      
      self.texture = tex
#      print 'floor init'
      self.transforms = [0.,0.,0.,0.,0.,0.,1.0]
      self.transp = True
      self.color = [1.,1.,1.,1.]
   
   def draw(self):
   
      transparency(self.transp)
      color(self.color)
      self.texture.bind()
      self.buffer.draw(style='solid') 
      self.texture.unbind()
      
   def step(self):
      if self.color[3] < 1.:
         self.color[3] += .001
      else:
         pass


