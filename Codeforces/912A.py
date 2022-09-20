
a , b = map(int , input().split())

x = [int(x) for x in input().split()]

y = 2 * x[0] + x[1] - a

if y < 0:
    y = 0

bl = x[1] + 3 * x[2] - b
if bl < 0:
    bl = 0
print(y + bl)