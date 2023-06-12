first = 1
second = 1
sum = 0

while second < 4000000:
    next = first + second
    first = second
    second = next
    if next % 2 == 0:
        sum = sum + next

print(sum)

# answer: 4613732