import time
start = time.time()
count = 0
'''we will iterate to 9*10**7 because there are no solutions above 10**8'''

for i in range(1, 9*10**7):
    if i % 10 == 0:
        continue
    last = i % 10
    stri = str(i)
    first = int(stri[0])
    if (first + last) % 2 == 0:
        continue
    if (first + last) % 10 == 0:
        continue
    sum = i + int(stri[::-1])
    sum = str(sum)
    if '0' in sum or '2' in sum or '4' in sum or '6' in sum or '8' in sum:
        continue
    else:
        count += 1
end = time.time()
print(count)
print(end - start)

# answer: 608720
# time: 67.99s

