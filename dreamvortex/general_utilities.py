'''
Generally useful functions for vroom programs
Dawn Sumner, Djerassi, July 2014
'''

from vroom import *
from math import sqrt

###### Transform Drawing Location ######
def transform(item):
   '''Performs the OpenGL transformations to place objects 
   in the correct locations for Vroom
   Input format: [[x,y,z],[rx,ry,rz],s] where 
         x,y,z gives translations
         rx,ry,rz gives rotations around the x, y and z axes, respectively
         s gives the scaling factor
   '''
   
   # list of transformations to apply
   trans=[translate, rotate, scale]
   
   #try each one
   for i in range(len(trans)):
      try:
         trans[i](item.transforms[i])        
      except:
#         pass
         print 'except', trans[i],i
   
######
def distance(obj1,obj2):
   dist = sqrt(sum([(a-b)*(a-b) for a,b in zip(obj1, obj2)])) 
   return dist
