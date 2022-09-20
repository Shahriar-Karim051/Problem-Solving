
a = int(input())

x = [int(x) for x in input().split()]
m = 1
c = 0

l = []
for i in x:
    if i == 1:
        m = m * 1
    elif i == -1:
        m = m * (-1)
    elif i > 1:
        c = (i - 1) + c
        
    elif i < -1:
        c = (i * (-1) - 1) + c
        m = m * (-1)
    elif i == 0:
        l.append(i)
        

if m == -1:
    if len(l) == 0:
        print(c + 2)
    else:
        print(c + len(l))
else:
    print(c + len(l))
        