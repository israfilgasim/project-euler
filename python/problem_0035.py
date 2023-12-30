import time

start = time.time()

lst = [2]
def is_prime(n):
    for prime in lst:
        if n % prime == 0:
            return False
        if prime ** 2 > n:
            break
    return True

for num in range(3,10**6,2):
    if is_prime(num):
        lst.append(num)

count = 0

for prime in lst:
    prime = str(prime)
    for i in range(len(prime)):
        prime = prime[-1] + prime[:-1]
        if int(prime) not in lst:
            break
    else:
        count += 1

end = time.time()
print(count)
print(end - start)

# answer: 55
# runtime: 63.6s

