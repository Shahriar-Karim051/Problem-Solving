
from operator import itemgetter

n = int(input())
l = []

for i in range(n):
    x = [int(x) for x in input().split()]
    l.append(x)
    
b = sorted(l , key=itemgetter(1))
b = sorted(b , key = itemgetter(0))

c = [item[0] for item in b]

d = [item[1] for item in b]

best = -1
for i in range(len(d)):
    if best <= d[i]:
        best = d[i]
    else:
        best = c[i]
        
print(best)
    
    
    