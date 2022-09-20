

n , m = map(int , input().split())

a = n // m
b = n % m
l = []
for i in range(m):
    if b > 0:
        l.append(a + 1)
        b -= 1
    else:
        l.append(a)
        
l.sort()

for i in l:
    print(i , end = ' ')
    
    