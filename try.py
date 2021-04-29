import time


now = time.time()
print(now)
time.sleep(1)
later = time.time()
print(later)
difference = later - now
print(difference)
