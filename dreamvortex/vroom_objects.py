'''
Base class(es) for graphical objects in vroom
Dawn Sumner, Djerassi, July 2014

Idea: 
Graphical objects have a:
   description, with special features such as multiple points, colors, textures, etc
   position for the "center of mass" of the object relative to the point locations
   rotation relative to the point locations
   scale relative to the point locations
In openGL and with graphics cards, it is computationally efficient to keep the original object description and translate/rotate/scale where it is drawn rather than recalculate the locations of all the points in the object.  

Thus, create a graphical object class for Vroom to hold the description plus transformations in a uniform structure so that they can be systematically drawn.

'''

class GraphicalObjects:

   def __init__(self):
      '''Base class for graphical objects in Vroom, including:
      description, position, rotation, and scale
      '''
   
      self.desc = []
      self.pos = []
      self.rot = []
      self.scale = []
      
#      self.append() = append()   # How do I create a function .append for this class?
      
   def append(self, desc, pos = [0.,0.,0.], rot = 0., scale = 1.):
      '''puts all the necessary parts into the graphical object
      '''
      self.desc = desc
      self.pos = pos
      self.rot = rot
      self.scale = scale
      
   def write(self,form = 'graphical'):
      '''writes out graphical objects with the format:
         graphical - with desc, pos, rot, scale
         transformed - the object description with points transformed by pos, rot, scale
      '''
      raise NotImplementedError()

   def read(self):
      '''reads in graphical objects written by write
      '''
      raise NotImplementedError()
      
   def draw(self):
      '''draws a graphic object using desc with the transformations applied
      as defined by pos, rot, scale
      ''' 
      raise NotImplementedError()
    
      
