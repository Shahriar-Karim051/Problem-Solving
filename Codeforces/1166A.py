
from collections import Counter

n = []

for i in range(int(input())):
    a = input()
    n.append(a[0])
    
cnt = 0
p = Counter(n)
#print(p)
for i in p:
    if p[i] > 2:
        f = p[i] // 2
        s = p[i] - f
        cnt += (f * (f - 1)) / 2 + (s * (s - 1)) / 2
        
print(int(cnt))
