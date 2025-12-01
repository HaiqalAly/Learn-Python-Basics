# Countdown Timer Exercise

import time

timer = int(input("Enter the time in seconds for the countdown: "))

for x in range(0, timer):
    print(f"Time left: {timer - x} seconds")
    time.sleep(1)

print("Time's up!")