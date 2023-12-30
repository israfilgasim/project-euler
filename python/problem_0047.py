count = 0 # number of consecutive numbers with 4 distinct prime factors

for i in range(1, 1000000):
    temp = i # temp variable to store i
    divs = 0 # number of distinct prime factors

    if i % 2 == 0:
        divs = 1
        while i % 2 == 0:
            i = int(i / 2)

    for j in range(3, 1000, 2):
        if i % j == 0:
            divs += 1
            while i % j == 0:
                i = int(i / j)
    if divs == 4:
        count += 1
    else:
        count = 0
    if count == 4:
        print(temp - 3)
        break

# answer: 134043
