max_chain = 0
for i in range(1, 1000000):
    chain = 0
    n = i
    while n != 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = 3 * n + 1
        chain += 1
    if chain > max_chain:
        max_chain = chain
        number = i
print(number)

# answer: 837799
