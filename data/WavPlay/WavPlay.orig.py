# WavPlay.py: Access and play *.wav sounds files, randomly
#

import pygame
from pygame import *
import sys,time
from random import randrange

# Read in list of wav files
f = open(sys.argv[1])
WavFilenames = []
for line in f:
	WavFilenames.append(line[:-1])

nFiles = len(WavFilenames)

pygame.mixer.pre_init(frequency=44100,size=-16,channels=2,buffer=4096)
pygame.init()
pygame.mixer.init()
print pygame.mixer.get_init()
#screen = pygame.display.set_mode((400,400),0,32)

# Randomly select and open a subset (to keep memory needs down)
nPlay = 20
print "Playing",nPlay,"random samples, out of",nFiles, "*.wav files found"
WavSamples = []
for i in xrange(nPlay):
	sname = WavFilenames[randrange(0,nFiles)]
	WavSamples.append([pygame.mixer.Sound(sname),sname])

# Play a random sound file in the list WavSamples
#   Returns handle to channel
#
def RandPlay(WavSamples):
	sample = randrange(0,len(WavSamples))
	print "Playing ",WavSamples[sample][1]
	return WavSamples[sample][0].play()

RandPlay(WavSamples)
time.sleep(1)
RandPlay(WavSamples)
time.sleep(1)

MinDelay = 1
MaxDelay = 6

while True:
	ch = RandPlay(WavSamples)
	time.sleep(randrange(MinDelay,MaxDelay))
#	while ch.get_busy():
#		pygame.time.delay(1)
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		if event.type == KEYDOWN:
			if event.key == K_ESCAPE:
				pygame.quit()
				sys.exit()
#			elif event.key==K_UP:
#	pygame.display.update()
