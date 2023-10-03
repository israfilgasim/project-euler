sum = 1 # for storing 2^1000

for i in range(1,1001):
    sum *= 2

digitsum = 0 # for storing the sum of digits of 2^1000

while sum > 0:
    digitsum += sum % 10
    sum = sum // 10

print(digitsum)

# answer: 1366