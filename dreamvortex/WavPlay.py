# WavPlay.py: Access and play *.wav sounds files, randomly or not
# Sound files are now located in data/sounds and any of those files can be played
#     this version does not require a text file listing of sounds

import pygame
from pygame import *
import sys,time
from random import randrange

import os

# Samples loaded and their file names
WavSamples = []

def InitWavPlay(nPlay):       # note, doesn't take a file name
	'''Read sounds from folder using Jordan's init technique for images
	'''
	WavFilenames = [os.path.join('data/sounds', wav) for wav in os.listdir('data/sounds')]
#	print WavFilenames

	nFiles = len(WavFilenames)
	if nPlay >= nFiles: nPlay = nFiles - 1
	
	pygame.mixer.pre_init(frequency=44100,size=-16,channels=2,buffer=4096)
	pygame.init()
	pygame.mixer.init()
	print pygame.mixer.get_init()

	# Randomly select and open a subset (keep memory needs down)
	for i in xrange(nPlay):
		sname = WavFilenames[randrange(0,nFiles)]
		WavSamples.append([pygame.mixer.Sound(sname),sname])

	print "Can play",nPlay,"random samples, out of",nFiles, "*.wav files found"

# Play randomly selected sound file in the list WavSamples
#   Returns handle to channel
#
def RandPlay():
	sample = randrange(0,len(WavSamples))
#	print "Playing ",WavSamples[sample][1]
	return WavSamples[sample][0].play()

# Play a given sound file (in [0,nPlay-1])
#   Returns handle to channel
#
def PlayThis(sample):
	if(sample < 0 or sample >= len(WavSamples)):
		print "Sample",sample,"out of range [0,",len(WavSamples),"]"
	else:
		print "Playing ",WavSamples[sample][1]
		return WavSamples[sample][0].play()

############################################################
#
if __name__ == '__main__':
	print "Testing"
	nSamples = 10
	InitWavPlay("WavFiles.txt",nSamples)

	# Single play
	PlayThis(0)
	time.sleep(2)
	
	# Play randomly selected sample with random time between playing samples
	MinDelay = 1
	MaxDelay = 6
	while True:
		RandPlay()
		time.sleep(randrange(MinDelay,MaxDelay))
