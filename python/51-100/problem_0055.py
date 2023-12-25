import time

start = time.time()

lychrels = []

for i in range(1, 10000):
    n = i
    status = True
    for j in range(50):
        n += int(str(n)[::-1])
        if str(n) == str(n)[::-1]:
            status = False
            break
    if status:
        lychrels.append(i)

print(time.time() - start) # 0.0 seconds
print(len(lychrels)) # 249