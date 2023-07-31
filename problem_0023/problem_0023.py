import time

start_time = time.time()
all_numbers = [i for i in range(0, 28124)]

dividers = [0] * 28124

for i in range(1, 14062):
    for j in range(i * 2, 28124, i):
        dividers[j] += i

abundants = []

for num in range(1, 28124):
    if dividers[num] > num:
        abundants.append(num)

for num1 in range(0, len(abundants)):
    for num2 in range(num1, len(abundants)):
        sum1 = abundants[num1] + abundants[num2]
        if sum1 < 28124:
            all_numbers[sum1] = 0
end = time.time()
print(sum(all_numbers))
print(str(end - start_time) + " seconds")

# answer: 4179871
# ~ 4 seconds