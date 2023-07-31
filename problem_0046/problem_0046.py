import time
import itertools

start = time.time()

permutations = []

for perm in itertools.permutations(range(10)):
    string = ''
    for i in perm:
        string += str(i)
    if string[0] != '0':
        permutations.append(string)

sum = 0

for num in permutations:
    if int(num[1:4]) % 2 != 0:
        continue
    if int(num[2:5]) % 3 != 0:
        continue
    if int(num[3:6]) % 5 != 0:
        continue
    if int(num[4:7]) % 7 != 0:
        continue
    if int(num[5:8]) % 11 != 0:
        continue
    if int(num[6:9]) % 13 != 0:
        continue
    if int(num[7:]) % 17 != 0:
        continue
    sum += int(num)

end = time.time()
print(sum)
print(end - start)

# answer: 16695334890
# ~ 11 seconds