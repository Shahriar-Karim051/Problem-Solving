
n , m = input().split()

x = [int(x) for x in input().split()]
y = [int(y) for y in input().split()]

ex = ey = ox = oy = 0

for i in x:
    if i % 2 == 0:
        ex += 1
    else:
        ox += 1

for i in y:
    if i % 2 == 0:
        ey += 1
    else:
        oy += 1
        
print(min(ex , oy) + min(ox , ey))