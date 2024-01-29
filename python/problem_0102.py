import time


start = time.time()
count = 0
with open("problem_0102.txt", "r") as file:
    for line in file:
        triangle = [int(x) for x in line.split(",")]
        ax, ay, bx, by, cx, cy = triangle

        ao = (bx-ax)*(-ay) - (by-ay)*(-ax)
        bo = (cx-bx)*(-by) - (cy-by)*(-bx)
        co = (ax-cx)*(-cy) - (ay-cy)*(-cx)

        if (ao > 0 and bo > 0 and co > 0) or (ao < 0 and bo < 0 and co < 0):
            count += 1

print(time.time() - start) # 0.00 seconds
print(count) # 228

