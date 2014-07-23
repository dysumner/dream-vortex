from core import Settings
from vroom.utils.resources import get_resource
from vroom.rendering.texture import Texture
from random import randint

###### Load Settings ######
settings = Settings('vortex-settings.yaml')

def init_settings():
    print('dreamvortex: init_settings')
    global settings
    settings = Settings('vortex-settings.yaml')

def get_settings():
    return Settings('vortex-settings.yaml')
    
###### Load Emblem Data ######
emblem_data = Settings('emblems.yaml')

def init_emblem_data():
   print ('dreamvortex: init_emblem_data')
   global emblem_data
   emblem_data = Settings('emblems.yaml')

def get_emblem_data():
   return Settings('emblems.yaml')

###### Load Textures for Items ######
import os

# for full dream images
dream_images = [os.path.join('dreams', img) for img in os.listdir('data/dreams')]

dreams = None

def load_dreams():
   global dreams
   dreams = [Texture.from_file(get_resource(img)) for img in dream_images]
   return len(dreams)

def get_dream(i = None):  # 
   if i == None: i = randint(0, len(dreams)-1)
#   print 'i',i
   return dreams[i]
   
# for dream strips
strip_images = [os.path.join('strips', img) for img in os.listdir('data/strips')]

strips = []

def load_strips():
   global strips
   strips = [Texture.from_file(get_resource(img)) for img in strip_images]

def get_strip():
   return strips[randint(0, len(strips)-1)]

# for dreams on flat emblems
emblem_images = [os.path.join('emblems_flat', img) for img in os.listdir('data/emblems_flat')]

emblems_flat = []

def load_emblems_flat():
   global emblems_flat
   emblems_flat = [Texture.from_file(get_resource(img)) for img in emblem_images]

def get_emblem_flat():
   return emblems_flat[randint(0, len(emblems_flat)-1)]
   
# for mesh emblems - NOT COMPLETE
emblem_meshs = [os.path.join('emblems', mesh) for mesh in os.listdir('data/emblems')]
emblems = []

def load_emblems(): pass
#   global emblems
#   emblems = 

def get_emblem():
   pass
   
   


