from core import Settings
from vroom.utils.resources import get_resource
from vroom.rendering.texture import Texture
from random import randint

settings = Settings('vortex-settings.yaml')

def init_settings():
    print('dreamvortex: init_settings')
    global settings
    settings = Settings('vortex-settings.yaml')

def get_settings():
    return Settings('vortex-settings.yaml')

import os

dream_images = [os.path.join('dreams', img) for img in os.listdir('data/dreams')]

dreams = None

def load_dreams():
   global dreams
   dreams = [Texture.from_file(get_resource(img)) for img in dream_images]

def get_dream():
   return dreams[randint(0, len(dreams)-1)]
   
# Added to put dreams on strips
strip_images = [os.path.join('strips', img) for img in os.listdir('data/strips')]

strips = []

def load_strips():
   global strips
   strips = [Texture.from_file(get_resource(img)) for img in strip_images]

def get_strip():
   return strips[randint(0, len(strips)-1)]

