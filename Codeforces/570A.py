

can , city = map(int , input().split())

l = []

for i in range(can):
    l.append(0)
    
for i in range(city):
    x = [int(x) for x in input().split()]
    a = x.index(max(x))
    l[a] = l[a] + 1
    
print(l.index(max(l)) + 1)