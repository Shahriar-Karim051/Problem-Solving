
a , b = input().split()
a = int(a)
b = int(b)

x = [int(x) for x in input().split()]
x.sort()

if len(x) == 1:
    if x[0] == 0 or x[0] == b:
        print(float(b))
        exit()
    else:
        print(max(x[0] , b - x[0]))
        exit()
    
for i in range(a):
    if i == 0:
        mx = x[i] - 0
    elif i == a - 1:
        c = max((b - x[i]) , ((x[i] - x[i - 1]) / 2))
        if c > mx:
            mx = c
    else:
        if ((x[i] - x[i - 1]) / 2) > mx:
           mx = (x[i] - x[i - 1]) / 2
    
        

print(float(mx))
    
    
    