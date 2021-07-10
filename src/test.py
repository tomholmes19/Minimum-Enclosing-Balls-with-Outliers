from threading import Timer, Event
import time
import sys
timeout = 5
try:
    print("Start timer")
    time.sleep(timeout)
except KeyboardInterrupt:
    print("Caught exit")
    sys.exit()

print("aaah")