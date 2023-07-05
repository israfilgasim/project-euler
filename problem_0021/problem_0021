amicables = []


for num1 in range(1, 10000):
    
    mid1 = int(num1 ** 0.5) + 1
    divisors1 = []

    for i in range(1, mid1):
        if num1 % i == 0:
            divisors1.append(i)
            if int(num1 / i) != i and int(num1 / i) != num1:
                divisors1.append(int(num1 / i))
    
    num2 = 0
    for div1 in divisors1:
        num2 += div1

    mid2 = int(num2 ** 0.5) + 1
    divisors2 = []

    for m in range(1, mid2):
        if num2 % m == 0:
            divisors2.append(m)
            if int(num2 / m) != m and int(num2 / m) != num2:
                divisors2.append(int(num2 / m))

    num3 = 0
    for div2 in divisors2:
        num3 += div2
    
    if num1 == num3 and num1 != num2:
        amicables.append(num1)

print(amicables)
print(sum(amicables))

# answer: 31626
