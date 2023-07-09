# to solve the problem, we need function that checks if a number is prime or not

def is_prime(n):
    status = True # assume that n is prime
    
    sqrt = int(n ** 0.5) + 1 # we iterate until sqrt(n) because if n is not prime, it must have a factor less than or equal to sqrt(n)

    for i in range(3, sqrt, 2):
        if n % i == 0:
            status = False
            break
    return status

sum = 2

for i in range(3, 2000000, 2):
    if is_prime(i):
        sum += i

print(sum)

# answer: 142913828922