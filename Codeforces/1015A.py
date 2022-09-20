
n , m = map(int , input().split())

p = []
q = []
for i in range(n):
    l , r = map(int , input().split())
    for j in range(l , r + 1):
        p.append(j)
            
for i in range(1 , m + 1):
    if i not in p:
        q.append(i)
        
print(len(q))

for i in q:
    print(str(i) , end = ' ')