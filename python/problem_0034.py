lst = []

for i in range(3, 1000000):
    sum = 0
    temp = i

    while temp > 0:
        digitsum = 1
        digit = temp % 10
        while digit > 0:
            digitsum *= digit
            digit -= 1
        sum += digitsum
        temp //= 10
    
    if sum == i:
        lst.append(i)

print(lst)

# Output: [145, 40585] ans = 145 + 40585 = 40730
            