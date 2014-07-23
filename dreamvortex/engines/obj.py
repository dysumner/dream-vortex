'''
Test object for Vroom GraphicalObjects
Dawn Sumner, Djerassi, July 2014
'''

from dreamvortex.engines.engine import BaseItem
from vroom.rendering.point_cloud import PointCloud

class Obj (BaseItem):
   
   def __init__(self):
   
      # run the __init__ of the inherted class
      BaseItem.__init__(self, None, None)
   
      # make some vertices
      self.vert = [[1,1,0],[1,-1,0],[-1,1,0],[-1,-1,0],[0,0,1]]
      self.color = [[1,1,0],[1,0,0],[0,1,0],[1,1,1],[0,0,1]]
      
      #set up opengl transformations
      #     [translate [x,y,z] or [distance, [direction]], 
      #     rotate [x-axis,y-axis,z-axis], 
      #     scale [x,y,z] or real]
      self.transforms = [[0.,0.,0.],[0.,0.,0.],1.] 
      
      # ^ probably better to implement as a dictionary with names for the transforms so that some can be left out without shifting all the other values



   def step(self):
      '''Items to animate the object'''
      pass
      
   def draw(self):
   
      # define the buffer and draw the points
      self.buffer = PointCloud(self.vert) #why can't i pass in color?
      self.buffer.sprite('data/particle.bmp')
      self.buffer.pointSize(50.0)
      self.buffer.draw()
      
   def move_obj(self, trans=[0,0,0]):
      
      vert = []
   
      # this gives the new point locations
      for point in self.vert:
         new_point = []
         for i,j in zip(point,trans):
            new_point.append(i+j)
         vert.append(new_point) 
      
      self.vert = vert
#      print 'translate by', trans

