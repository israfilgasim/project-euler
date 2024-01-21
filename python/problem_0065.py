convergents = [[2,1], [3,1],[8,3], [11,4], [19,7]]

last = 4
for i in range(6,101):
    if i % 3 == 0:
        denominator = convergents[-1][1] * last + convergents[-2][1]
        numerator = convergents[-1][0] * last + convergents[-2][0]
        last += 2
        convergents.append([numerator, denominator])
    else:
        denominator = convergents[-1][1] + convergents[-2][1]
        numerator = convergents[-1][0] + convergents[-2][0]
        convergents.append([numerator, denominator])


totalsum = 0
temp = convergents[-1][0]

while temp > 0:
    totalsum += temp % 10
    temp = temp // 10


print(totalsum) # 272