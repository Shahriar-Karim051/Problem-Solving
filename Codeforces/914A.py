
import math
n = int(input())
a = [int(a) for a in input().split()]
a.sort()
for i in a:
    if i < 0:
        ps = i
    else:
        x = math.sqrt(i)
        if x != int(x):
            ps = i
        
        
print(ps)