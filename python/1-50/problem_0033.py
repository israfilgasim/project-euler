import time

start = time.time()

lst = []

for i in range(10, 100):
    if i % 10 == 0 or i % 11 == 0:
        continue
    for j in range(i-1, 10,-1):
        if j % 10 == 0 or j % 11 == 0:
            continue
        newa = str(i)
        newb = str(j)
        if len(set(newa + newb)) != 3:
            continue
        else:
            a = ""
            b = ""
            for l in newa:
                if l not in newb:
                    a += l
            for m in newb:
                if m not in newa:
                    b += m
            k = i / j
            z = int(a) / int(b)
            if k == z:
                lst.append([i, j])


print(time.time() - start) # 0.0 seconds
print(lst) # [[16, 64], [19, 95], [26, 65], [49, 98]] 100