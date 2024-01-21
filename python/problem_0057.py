import time
start = time.time()


numerator = 3
denumerator = 2

nth = 1

exceeds = []

while nth < 1000:
    denumerator = numerator + denumerator
    numerator = 2*denumerator - numerator

    if len(str(numerator)) > len(str(denumerator)):
        exceeds.append([numerator, denumerator])
    nth += 1

print(time.time() - start) # 0.00 seconds
print(len(exceeds)) # 153
