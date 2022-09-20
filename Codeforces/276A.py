
a , b = input().split()
a = int(a)
b = int(b)
x = [int(x) for x in input().split()]
if x[1] <= b:
    best = x[0]
else:
    best = x[0] - (x[1] - b)
for i in range(a - 1):
    x = [int(x) for x in input().split()]
    if x[1] <= b:
        c = x[0]
    else:
        c = x[0] - (x[1] - b)
    if c > best:
        best = c
        
print(best)
    