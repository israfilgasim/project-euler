import time

start = time.time()

words = []

with open("problem_0042.txt", "r") as file:
    k = file.read().split(",")
    for i in k:
        words.append(i[1:-1])

triangles = [1]
counter = 2
last = 1

while last < 1000:
    last += counter
    counter += 1
    triangles.append(last)


triangle_words = 0

for word in words:
    a = sum([ord(i) - 64 for i in word])
    if a in triangles:
        triangle_words += 1


print(time.time() - start) # 0.002 seconds
print(triangle_words) # 162
