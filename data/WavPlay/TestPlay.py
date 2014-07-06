# TestPlay.py: Access and play *.wav sound files from cmd line
#

import pygame
from pygame import *
import sys,time

SoundFile1 = sys.argv[1]
SoundFile2 = sys.argv[2]

pygame.mixer.pre_init(frequency=44100,size=-16,channels=2,buffer=4096)
pygame.init()
pygame.mixer.init()
print SoundFile1, SoundFile2
print pygame.mixer.get_init()
screen = pygame.display.set_mode((400,400),0,32)

sa = pygame.mixer.Sound(SoundFile1)
sb = pygame.mixer.Sound(SoundFile2)
sa.play()
time.sleep(2)
sb.play()

while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		if event.type == KEYDOWN:
			if event.key == K_ESCAPE:
				pygame.quit()
				sys.exit()
			elif event.key==K_UP:
				cha = sa.play()
				time.sleep(2)
				chb = sb.play()
				while chb.get_busy():
					pygame.time.delay(1)
	pygame.display.update()
