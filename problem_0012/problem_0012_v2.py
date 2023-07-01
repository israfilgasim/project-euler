'''
N = p₁^a₁ * p₂^a₂ * p₃^a₃ * ... * pₙ^aₙ

where p₁, p₂, ..., pₙ are prime numbers, and a₁, a₂, ..., aₙ are their respective powers.

To find the number of divisors (D) for this number, we can use the formula:

D = (a₁ + 1) * (a₂ + 1) * (a₃ + 1) * ... * (aₙ + 1)
'''

sum = 0

for i in range(1, 100000):
    sum = sum + i
    primeFactors = []
    n = sum
    if n % 2 == 0:
        count = 0
        while n % 2 == 0:
            count += 1
            n = n // 2
        primeFactors.append(count)
    for j in range(3, int(n**0.5)+1, 2):
        if n % j == 0:
            count = 0
            while n % j == 0:
                count += 1
                n = n // j
            primeFactors.append(count)
    divsiors = 1

    for k in primeFactors:
        divsiors = divsiors * (k + 1)
    
    if divsiors > 500:
        print(sum)
        exit()

# answer: 76576500