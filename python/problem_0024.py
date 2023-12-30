import math

nth = 0

i = 0
digitNth = 1
digits = [0,1,2,3,4,5,6,7,8,9]
millionth = []

while nth < 1000000:
    fact = 10 - digitNth
    nth += math.factorial(fact)
    i += 1
    if nth + math.factorial(fact) >= 1000000:
        temp = digits[i]
        del digits[i]
        millionth.append(temp)
        i = 0
        digitNth += 1
    if len(digits) == 1:
        millionth.append(digits[0])
        break

print(millionth)

# answer: 2783915460