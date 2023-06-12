# we write function to find greatest prime factor of a number

def greatestPrimeFactor(num):
    lst = []
    if num % 2 == 0:
        lst.append(2)
        while num % 2 == 0:
            num = num / 2

    #we add 2 every time because we know that 2 is the only even prime number
    #we iterate this until square root of number, because the largest prime factor of a number is less than or equal to its square root
    
    for i in range(3, int(num ** 0.5) + 1, 2): 
        if num % i == 0:
            lst.append(i)
            while num % i == 0:
                num = num / i
    # for understanding deeply, I don't use max function (I know it is not good)

    max = 0
    for i in lst:
        if i > max:
            max = i
    return max

print(greatestPrimeFactor(600851475143))

# answer: 6857