import time

start = time.time()

months = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

count = 0
year = 1900
month = 1
day = 1
weekday = 1

while year < 2001:
    month = 1
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        months[2] = 29
    else:
        months[2] = 28
    
    while month < 13:
        day = 0
        while day < months[month]:
            day += 1
            weekday += 1
            if day == 1 and weekday == 7 and year > 1900:
                count += 1
            if weekday == 7:
                weekday = 0
        month += 1
    year += 1

print(time.time() - start) # 0.00 seconds
print(count) # 171
