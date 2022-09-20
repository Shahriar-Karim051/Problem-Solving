
n , a , b = map(int , input().split())

x = [int(x) for x in input().split()]
y = [int(y) for y in input().split()]

l = [0] * n

for i in x:
    l[i - 1] = 1
    
for j in y:
    if j not in x:
        l[j - 1] = 2
        
print(*l)
    