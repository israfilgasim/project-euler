txt = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""

txt = txt.split("\n")

lst = []

for i in range(len(txt)):
    lst.append(txt[i].split(" "))

sum = int(lst[0][0])
last = 0

for i in range(1, len(lst) - 1):
    way1a = int(lst[i][last]) + int(lst[i + 1][last])
    if lst[i + 1][last + 1] != None:
        way1b = int(lst[i][last]) + int(lst[i + 1][last + 1])
    else:
        way1b = 0
    if lst[i][last + 1] != None and lst[i + 1][last + 1] != None:
        way2a = int(lst[i][last + 1]) + int(lst[i + 1][last + 1])
    else:
        way2a = 0
    if lst[i][last + 1] != None and lst[i + 1][last + 2] != None:
        way2b = int(lst[i][last + 1]) + int(lst[i + 1][last + 2])
    else:
        way2b = 0
    big = max(way1a, way1b, way2a, way2b)
    if big == way1a:
        sum += int(lst[i][last])
        last = last
    elif big == way1b:
        sum += int(lst[i][last])
        last = last
    elif big == way2a:
        sum += int(lst[i][last + 1])
        last = last + 1
    elif big == way2b:
        sum += int(lst[i][last + 1])
        last = last + 1

sum += max(int(lst[len(lst) - 1][last]), int(lst[len(lst) - 1][last + 1]))

print(sum)

# answer: 1074