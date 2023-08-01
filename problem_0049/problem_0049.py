import time
start = time.time()
primes = []

for i in range(1001, 10000, 2):
    mid = int(i ** 0.5) + 1
    status = True
    for j in range(3, mid, 2):
        if i % j == 0:
            status = False
            break
    if status == True:
        primes.append(i)

for i in range(len(primes)):
    second = primes[i] + 3330
    third = second + 3330
    if second in primes and third in primes:
        if sorted(str(primes[i])) == sorted(str(second)) and sorted(str(primes[i])) == sorted(str(third)):
            print(primes[i], second, third)

end = time.time()
print(end - start)


# answers : 1487 4817 8147 and 2969 6299 9629
# runtime : 0.02s