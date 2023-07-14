powers = []

for a in range(2, 101):
    for b in range(2, 101):
        powers.append(a**b)

print(len(set(powers)))

# answer: 9183