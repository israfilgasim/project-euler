import time

start = time.time()

solutions = []

for i in range(1, 10000): # 10000, because 10000 * 1 and 10000 * 2, which are 5 digits each, would be 10 digits, which is too much
    n = 1
    st = ""
    while len(st) < 9:
        st += str(i * n)
        n += 1
    if len(st) == 9 and len(set(st)) == 9 and "0" not in st:
        solutions.append(int(st))

print(time.time() - start) # 0.00 seconds
print(max(solutions)) # 932718654
 
