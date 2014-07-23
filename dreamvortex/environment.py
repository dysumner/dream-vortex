'''
functions for drawing comment environment elements for the dream vortex
Dawn Sumner, Djerassi, July 2014
'''

from vroom import *

def draw_floor(texture):
   # an image
   points = [[-50.,-50., 0.],[50., -50., 0.],[-50., 50., 0.],[50.,50.,0.]]
   coords = [[0.,0.],[1.,0.],[0.,1.],[1.,1.]]
   floor = Buffer(points)
   floor.loadTexCoordData(coords)
   floor.renderMode('triangles:strip')
   
   transparency(True)
   color(1.0)
   texture.bind()
   floor.draw(style='solid')
   texture.unbind()

def draw_grid():
   # a grid
   color(0.3) 
   draw(grid, 40, 40, 20, 20).at([-20, -20, 0])


