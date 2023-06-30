lst = []
sum = 0
c = set(['1','2','3','4','5','6','7','8','9'])

for i in range(1, 5000): # becuase 5000 * 2 = 10000 which is the max number of digits
    for j in range(i, 5000): # we start from i to avoid duplicates
        digits = str(i) + str(j) + str(i*j)
        if len(digits) == 9 and set(digits) == c:
            if i*j not in lst:
                sum += i*j
                lst.append(i*j)
                print(i, j, i*j)

print(sum) # 45228
print(lst) # [6952, 7852, 5796, 5346, 4396, 7254, 7632]
