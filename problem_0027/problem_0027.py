import time

start = time.time()

def isPrime(n):
    if n == 1 or n == 0:
        return False
    if n % 2 == 0:
        return False
    mid = int(n ** 0.5) + 1
    for i in range(3, mid, 2):
        if n % i == 0:
            return False
    return True
lst = []
max = 0
for a in range(-999,1000):
    for b in range(-1000,1001):
        status = True
        n = 0
        count = 0
        while status == True:
            eq = n ** 2 + a * n + b
            if eq < 0:
                status = False
            elif isPrime(eq) == False:
                status = False
            else:
                count += 1
                n += 1
        if count > max:
            max = count
            lst = [a,b]

end = time.time()
print(count, lst, lst[0] * lst[1])
print(end - start)

# 71 [-61, 971] -59231
# 2.4s


