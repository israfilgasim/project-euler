import time

start = time.time()

sum = 0

for i in range(1,1001):
    sum += i ** i

st = ""

while len(st) < 10:
    st = str(sum % 10) + st
    sum //= 10

end = time.time()

print(end - start) # 0.01 seconds
print(st) # 9110846700