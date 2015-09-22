'''
Generally useful functions for vroom programs
Dawn Sumner, Djerassi, July 2014
'''

from vroom import *
from math import sqrt

###### Transform Drawing Location ######
def transform(item):
   '''
   Performs transformations on environments prior to drawing objects 
   
   Input format: [[x,y,z],[rx,ry,rz],s] where 
         x,y,z gives translations
         rx,ry,rz gives rotations around the x, y and z axes, respectively
         s gives the scaling factor
         
   Transformations coded in this order:
      translateX, translateY, translateZ, rotateX, rotateY, rotateZ, scale
   Since the transformations apply to the environment when placed around a draw()
   statement, it's like doing the reverse order if they were applied to the object.
   
   General Reminder:
   translations are communitive within themselves but not with rotations and scaling
   scaling is communitive with rotations as a group
   individual rotations are not communitive
   
   The approach for transforming objects relative to each other: NEED TO TEST
      transform to the desired final position in Vrui space
         (moves the draw origin to that location)
      rotate the axes so the object is drawn at the proper orientation
      scale the units on the axes so the object is drawn at the proper scale
      transform the axes so that the origin of the object is the origin of the axes
         (if it isn't already. If the object is offset, rotations won't work right)
   '''
   
   # list of transformations to apply
   trans=[translate, rotate, scale]
   
   #try each one
   for i in range(len(trans)):
      try:
         trans[i](item[i]) #.transforms[i])        
      except:
         pass
#         print 'except', trans[i],i
   
######
def distance(obj1,obj2):
   dist = sqrt(sum([(a-b)*(a-b) for a,b in zip(obj1, obj2)])) 
   return dist
   
######
def invert(v):
   v = [-i for i in v]
   return v
   
