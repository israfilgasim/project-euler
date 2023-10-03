# first of all we iterate numbers from 1 to 9
# because 10^1 = 10, 10^2 = 100, 10^3 = 1000, 10^4 = 10000, 10^5 = 100000, 10^6 = 1000000
# so, after 9 we will have more digits than power

count = 0

for i in range(1, 100): # i is power
    for j in range(1, 100): # we need to iterate numbers from 1 to 9, but we can iterate from 1 to 100
        if len(str(j ** i)) == i:
            count += 1
            print(count, j, i, j ** i)

#answer is 49