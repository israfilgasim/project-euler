# first of all, we will write a function that will control number is infinite or not

def isArriveOne(n):
    sum = 0
    while n > 0:
        sum += (n % 10) ** 2
        n //= 10
    if sum == 1:
        return True
    elif sum == 89:
        return False
    else:
        return isArriveOne(sum)

falseList = [] # this list will contain the numbers that will arrive 89

for i in range(1, 10000000):
    if isArriveOne(i) == False:
        falseList.append(i)

print(len(falseList)) # 8581146