import time

start = time.time()

triangle = []

with open("problem_0067.txt") as f: # you can see txt file in the same folder with code
    for line in f.readlines():
        triangle.append([int(i) for i in line.split()])

l = len(triangle)

for i in range(1,l):
    lenofrow = len(triangle[i])
    for j in range(lenofrow):
        if j == 0:
            triangle[i][j] = triangle[i][j] + triangle[i-1][j]
        elif j == lenofrow-1:
            triangle[i][j] = triangle[i][j] + triangle[i-1][j-1]
        else:
            triangle[i][j] = triangle[i][j] + max(triangle[i-1][j-1], triangle[i-1][j])

print(time.time()-start) # 0 seconds
print(max(triangle[-1])) # 7273