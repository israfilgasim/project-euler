list_t = []
for i in range(1,100000):
    t = (i * (i + 1)) / 2
    list_t.append(int(t))

list_p = []
for j in range(1,100000):
    p = (j * (3*j - 1)) / 2
    list_p.append(int(p))

list_h = []
for k in range(1,100000):
    h = (k * (2*k - 1))
    list_h.append(int(h))

same = []

for tri in list_t:
    if tri in list_p and tri in list_h:
        a = list_t.index(tri)
        same.append(a)

print(same) # [0, 284, 55384] our 1st element is 0 because arrays start at 0, therefore 55385 is the 55384th element

#answer: 55385*(55385+1)/2 = 1533776805
