

a = int(input())

x = [int(x) for x in input().split()]
d = s = 0
for i in range(a):
    if i % 2 == 0:
       d = d + max(x[0] , x[-1])
       if x[0] >  x[-1]:
           x.pop(0)
       else:
           x.pop(-1)
    else:
        s = s + max(x[0] , x[-1])
        if x[0] > x[-1]:
            x.pop(0)
        else:
            x.pop(-1)
    
print(d , s)
    
