import time

start = time.time()

matrix = []

with open("problem_0081.txt", "r") as file:
    for line in file:
        matrix.append([int(x) for x in line.split(",")])


for i in range(80):
    for j in range(80):
        if i == 0 and j == 0:
            continue
        elif i == 0:
            matrix[i][j] += matrix[i][j-1]
        elif j == 0:
            matrix[i][j] += matrix[i-1][j]
        else:
            matrix[i][j] += min(matrix[i][j-1], matrix[i-1][j])

print(time.time() - start) # 0.00 seconds    
print(matrix[-1][-1]) # 427337
