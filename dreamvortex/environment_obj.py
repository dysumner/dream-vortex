'''
functions for drawing comment environment elements for the dream vortex
Dawn Sumner, Djerassi, July 2014
'''

from vroom import *
#from dreamvortex.engines.engine import BaseItem, BaseEngine

class Floor:

   def __init__(self):
      points = [[-50.,-50., 0.],[50., -50., 0.],[-50., 50., 0.],[50.,50.,0.]]
      coords = [[0.,0.],[1.,0.],[0.,1.],[1.,1.]]
      self.buffer = Buffer(points)
      self.buffer.loadTexCoordData(coords)
      self.buffer.renderMode('triangles:strip')
      
#      self.texture = None  # initialize texture but can't assign it yet
      
      self.transforms = [0.,0.,0.,0.,0.,0.,1.0]
      self.transp = True
   
   def draw(self):
   
      transparency(self.transp)
      color(1.0)
      self.texture.bind()
      self.buffer.draw(style='solid') 
      self.texture.unbind()
      
   def step(self):
      pass


