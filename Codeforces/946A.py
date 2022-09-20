

n = int(input())

a = [int(a) for a in input().split()]
b = c = 0
for i in a:
    if i < 0:
        c += i
    else:
        b += i
        
print(b - c)