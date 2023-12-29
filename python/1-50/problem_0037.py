import time

start = time.time()

def isPrime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    mid = int(n ** 0.5) + 1
    for i in range(2, mid):
        if n % i == 0:
            return False
    return True

lst = []
count = 0
num = 13

while count < 11:
    if isPrime(num) == True:
        status = True
        st = str(num)
        l = len(st)
        r = l * -1
        for x in range(l):
            n = int(st[x:])
            if isPrime(n) == False:
                status = False
                break
        if status == False:
            num += 2
            continue
        for y in range(-1,r,-1):
            n = int(st[:y])
            if isPrime(n) == False:
                status = False
                break
        if status == False:
            num += 2
            continue
        else:
            lst.append(num)
            count += 1
    num += 2

print(sum(lst)) # 748317
print(time.time() - start) # 2.35 seconds
print(lst) # [23, 37, 53, 73, 313, 317, 373, 797, 3137, 3797, 739397]