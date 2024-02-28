import time
import math
start = time.time()

count = 0

for n in range(2, 101):
    for r in range(1, n):
        if math.comb(n, r) > 1000000:
            count += 1

print(time.time() - start) # 0.001 seconds
print(count) # 4075
