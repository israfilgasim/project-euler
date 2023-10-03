lst = []
a = 1
b = 2
c = 997

while a < (c - 1):
    b = a + 1
    while b < c:
        c = 1000 - a - b
        if a * a + b * b == c * c:
            z = [a, b, c]
            lst.append(z)
        b += 1
    a += 1

print(lst)
print(lst[0][0] * lst[0][1] * lst[0][2])

# answer: 31875000
# numbers: a = 200, b = 375, c = 425
