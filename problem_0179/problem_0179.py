import time
divisors = [0] * (10 ** 7) # we start from 2
start = time.time()
for i in range(1, 10**7):
    for j in range(i, 10**7, i):
        divisors[j] += 1

count = 0

for k in range(len(divisors) - 2):
    if divisors[k] == divisors[k + 1]:
        count += 1
end = time.time()
print(count)
print(str(int(end - start)) + " seconds")

# answer: 986262
# runtime: 37 seconds

