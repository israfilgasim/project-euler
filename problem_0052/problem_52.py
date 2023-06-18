for i in range(1000000):
    x = list(str(i))
    x2 = []
    x3 = []
    x4 = []
    x5 = []
    x6 = []
    sum = 0
    a = 2 * i
    while a > 0:
        k = a % 10
        x2.append(str(k))
        a = a // 10
    a = 3 * i
    while a > 0:
        k = a % 10
        x3.append(str(k))
        a = a // 10
    a = 4 * i
    while a > 0:
        k = a % 10
        x4.append(str(k))
        a = a // 10
    a = 5 * i
    while a > 0:
        k = a % 10
        x5.append(str(k))
        a = a // 10
    a = 6 * i
    while 6 * a > 0:
        k = a % 10
        x6.append(str(k))
        a = a // 10
    if ((len(x) == len(x2) and len(x) == len(x3)) and (len(x) == len(x4) and len(x) == len(x5))) and len(x) == len(x6):
        if ((set(x) == set(x2) and set(x2) == set(x3)) and (set(x3) == set(x4) and set(x4) == set(x5))) and set(x5) == set(x6):
            print(i)
            break



