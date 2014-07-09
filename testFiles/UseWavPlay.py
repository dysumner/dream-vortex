# UseWavPlay.py: Example of how to use WavPlay.py
#    No graceful exit, to keep example simple: Just Control-C out.
# Modified to read the files from a folder in data/sounds

from WavPlay import InitWavPlay,RandPlay,PlayThis
import time
from random import randrange

# Initialize WavPlay from list of files, choose size of subset to play
nSamples = 20
#InitWavPlay("WavFiles.txt",nSamples)
InitWavPlay(nSamples)

PlayThis(0)
time.sleep(2)

# Random time between playing samples
MinDelay = 1
MaxDelay = 10
   	
while True:
	RandPlay()
	time.sleep(randrange(MinDelay,MaxDelay))
