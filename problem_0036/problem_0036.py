import time
start = time.time()

def binaryCalculator(number):
    binary = ''
    while number > 0:
        binary = str(number % 2) + binary
        number //= 2
    return binary

db_palindromes = []
for i in range(1, 1000000, 2):
    if str(i) == str(i)[::-1]:
        binary = binaryCalculator(i)
        if binary == binary[::-1]:
            db_palindromes.append(i)

print(db_palindromes)
print(sum(db_palindromes))
end = time.time()
print(end - start)

# answer : 872187
# runtime : 0.2s