import time


# Dot Product Method
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

# Area Method
start = time.time()
count = 0

with open("problem_0102.txt", "r") as file:
    for line in file:
        triangle = [int(x) for x in line.split(",")]
        ax, ay, bx, by, cx, cy = triangle
        ox, oy = 0, 0

        area_abc = abs((ax-cx)*(by-ay) - (ax - bx)*(cy - ay))/2

        area_abo = abs((ax-bx)*(oy-ay) - (ax - ox)*(by - ay))/2
        area_bco = abs((bx-cx)*(oy-by) - (bx - ox)*(cy - by))/2
        area_aco = abs((ax-cx)*(oy-ay) - (ax - ox)*(cy - ay))/2

        if area_abc == area_abo + area_bco + area_aco:
            count += 1

print(time.time() - start) # 0.00 seconds
print(count) # 228

