import time

start = time.time()

maximum = 0
maxd = 0
nums = {}

for d in range(2,1000):
    count = 0
    st = "0."   
    i = 1
    quo = []

    while i < d:
        i *= 10
        if i > 10:
              
            st += "0"

    while True:
        k = i // d      
        st += str(k)
        count += 1
        if i == k * d:
            break   
        i = i - (k*d)
        if i in quo:
            break
        quo.append(i)   
       
        j = 0
        while i < d:      
            i *= 10
            j += 1
            if j > 1:
                st += "0" 
    if count > maximum:
        maximum = count
        maxd = d
    nums[d] = st


print(time.time() - start) # 0.13 seconds
print(maxd, maximum) # 983 885
             