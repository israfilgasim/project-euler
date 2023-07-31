import time

start = time.time()

for i in range(10**9, 10**10, 10):
    if str(i**2)[::2] == '1234567890':
        print(i)
        end = time.time()
        break

print(end - start)

# answer: 1389019170
# ~ 15.5 seconds
