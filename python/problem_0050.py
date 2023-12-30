import time

start = time.time()

def isPrime(n):
    if n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        mid = int(n**0.5)+1
        for i in range(3,mid,2):
            if n % i == 0:
                return False
    return True

primes = [2,3,5,7]

max_series = 0
max_prime = 0

for i in range(11,1000000,2):
    if isPrime(i):
        primes.append(i)

l = len(primes)

for i in range(l):
    for j in range(i+2,l+1):
        total = sum(primes[i:j])
        if total > 1000000:
            break
        if isPrime(total):
            cons = j - i
            if cons > max_series:
                max_series = cons
                max_prime = total

print(time.time()-start)
print(max_prime, max_series) # 997651 543