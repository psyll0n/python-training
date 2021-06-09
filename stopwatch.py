#! python3
# stopwatch.py - A simple stopwatch program.

import time

# Display the programs' instructions.
print(
    "Press ENTER to begin. Afterwards, press ENTER to 'click' the stop watch. Press Ctrl-C to quit."
)
input()  # press Enter to begin.
print("Timer Started...")
startTime = time.time()  # get the first lap's start time.
lastTime = startTime
lapNum = 1

# TODO: Start tracking the lap times.
try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        print("Lap #%s: %s (%s)" % (lapNum, totalTime, lapTime), end="")
        lapNum += 1
        lastTime = time.time()  # reset the last lap time.
except KeyboardInterrupt:
    # Handle the Ctrl-C exception to keep its error message from dispaying.
    print("\nDone. Stopwatch stopped.")
