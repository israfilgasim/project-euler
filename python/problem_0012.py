sum = 0

for i in range(1, 100000):
    sum = sum + i
    mid = int(sum**0.5) + 1
    divisors = []
    for j in range(1, mid):
        if sum % j == 0:
            divisors.append(j)
            if j != sum/j:
                divisors.append(sum/j)
            if len(divisors) > 500:
                print(sum)
                exit()
