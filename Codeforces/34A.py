
n = int(input())

x = [int(x) for x in input().split()]
x.append(x[0])
mn = abs(x[0] - x[1])
a = 1
b = 2
for i in range(len(x) - 1):
    h = abs(x[i] - x[i + 1])
    if h < mn:
        mn = h
        a = i % n + 1
        b = (i + 1) % n + 1
        
print(a , b)
        
    
    