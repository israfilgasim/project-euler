import time
start = time.time()

def isPrime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False

    return True


primes = [2, 3, 5, 7]

odd_comp = 9
while True:
    if isPrime(odd_comp):
        if odd_comp > primes[-1]:
            primes.append(odd_comp)
        odd_comp += 2
    else:
        status = True
        for p in primes:
            total = p + 2 * (1**2)
            if total == odd_comp:
                status = False
                break
            n = 2
            while total < odd_comp:
                total = p + 2 * (n**2)
                n += 1
                if total == odd_comp:
                    status = False
                    break
        if status:
            print(str(odd_comp) + " is the answer")
            break
        odd_comp += 2

print(time.time() - start) # 3.5 seconds
