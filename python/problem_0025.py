first = 1
second = 1
index = 2

while True:
    index += 1
    temp = first + second
    first = second
    second = temp
    if len(str(second)) >= 1000:
        print(second, index)
        break

# answer: 4782