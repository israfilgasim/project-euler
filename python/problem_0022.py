import time

start = time.time()

names = []

with open("problem_0022.txt", "r") as file:
    for line in file.readlines():
        k = line.split(",")
        for i in k:
            k = i[1:-1]
            names.append(k)


names.sort()

total = 0
nth = 1

for i in names:
    total += nth * sum([ord(j) - 64 for j in i])
    nth += 1

print("Time elapsed: ", time.time() - start) # 0.1 seconds
print(total) # 871198282