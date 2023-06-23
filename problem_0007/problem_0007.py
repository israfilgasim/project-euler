# to solve the problem, we need function that checks if a number is prime or not

def is_prime(n):
    status = True # assume that n is prime
    
    sqrt = int(n ** 0.5) + 1 # we iterate until sqrt(n) because if n is not prime, it must have a factor less than or equal to sqrt(n)

    for i in range(3, sqrt, 2):
        if n % i == 0:
            status = False
            break
    return status

nth = 1 # we start with 1 because 2 is the first prime number
n = 3 # every even number is not prime except 2
while nth <= 10000:
    if is_prime(n) == True:
        nth += 1
        number = n
    n += 2 # we only check odd numbers

print(number)

#answer: 104743
