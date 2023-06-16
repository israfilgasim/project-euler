# first of all, we have to find the upper bound of the number
# assume that the number is 9...9, then the upper bound is 9^5 * n = 10^n

upper = 1
while 9**5 * upper > 10**upper:
    upper += 1

print(upper) # 6, so the upper bound is 10^6 = 1000000

# then we can start to find the number

def digit_fifth_powers(n):
    lst = [] # for listing the numbers
    n = 10**n

    for i in range(2, n):
        sum = 0
        temp = i # for storing the number
        while temp > 0:
            sum += (temp % 10)**5
            temp //= 10
        if sum == i:
            lst.append(i)
    return lst

number_list = digit_fifth_powers(upper) # find the numbers

print(number_list) # [4150, 4151, 54748, 92727, 93084, 194979]

sum_of_numbers = 0

for i in number_list:
    sum_of_numbers += i

print(sum_of_numbers) # 443839