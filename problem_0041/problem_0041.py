import time
import itertools
start = time.time()

max = 2143

permutations = []

for i in range(5,10):
    for perm in itertools.permutations(range(1,i+1)):
        num = ''
        for digit in perm:
            num += str(digit)
        if int(num) % 2 != 0:
            permutations.append(int(num))

def isPrime(n):
    mid = int(n**0.5) + 1
    for i in range(3,mid,2):
        if n % i == 0:
            return False
    return True

for num in permutations:
    if isPrime(num) and num > max:
        max = num

end = time.time()

print(max)
print(end-start)

# answer: 7652413
# runtime: 1.1s
