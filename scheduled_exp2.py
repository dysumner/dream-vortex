from sched import scheduler
from threading import Thread
from time import time, sleep

schedule = scheduler(time, sleep)

# Set up a global to be modified by the threads
counter = 0

def increment_counter(name):
    global counter
    print 'EVENT:', time(), name
    counter += 1
    print 'NOW:', counter

print 'START:', time()
e1 = schedule.enter(0.05, 1, increment_counter, ('E1',))
e2 = schedule.enter(3, 1, increment_counter, ('E2',))

# Start a thread to run the events
t = Thread(target=schedule.run)
t.start()

# Back in the main thread, cancel the first scheduled event.
# scheduler.cancel(e1)

for i in range(10):
   counter += 1
   sleep(.5)

# Wait for the scheduler to finish running in the thread
#t.join()

print 'FINAL:', counter