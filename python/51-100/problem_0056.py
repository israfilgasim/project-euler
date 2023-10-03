import time

start = time.time()

max = 0

for a in range(2,100):
    for b in range(2,100):
        num = a**b
        sum = 0
        for digit in str(num):
            sum += int(digit)
        if sum > max:
            max = sum

end = time.time()

print(max)
print(end-start)

# answer: 972
# runtime: 0.1s