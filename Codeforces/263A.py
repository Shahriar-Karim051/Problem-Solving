l = []

for i in range(1,6):
    x = [int(x) for x in input().split()]
    if sum(x) == 1:
        a = x.index(1) + 1
        l.append(a)
        l.append(i)
        
#print(l)
print(abs(3 - l[0]) + abs(3 - l[1]))