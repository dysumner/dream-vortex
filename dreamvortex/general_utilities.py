'''
Generally useful functions for vroom programs
Dawn Sumner, Djerassi, July 2014
'''

from vroom import *

###### Transform Drawing Location ######
def transform(item):
   '''Performs the OpenGL transformations to place objects 
   in the correct locations for Vroom
   '''
   #probably better to implement as a dictionary with names for the transforms so that some can be left out without shifting all the other values - see vroom implementation of translate and rotate - they aren't what's written in documentation exactly
   
   # list of transformations to apply
   trans=[translateX,translateY,translateZ,
         rotateX, rotateY, rotateZ, scale]
   
   #try each one
   for i in range(len(trans)):
      try:
         trans[i](item.transforms[i])        
      except:
#         pass
         print 'except', trans[i],i
   
def distance(obj1,obj2):
   dist = ((obj1[0]-obj2[0])**2 + (obj1[0]-obj2[0])**2 + 
            (obj1[0]-obj2[0])**2)**0.5 
   return dist
