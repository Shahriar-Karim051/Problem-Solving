
n = int(input())

for i in range(n):
    x = [int(x) for x in input().split()]
    if x[0] < x[2]:
        a = 1
    elif x[0] % x[2] == 0:
        a = x[0] // x[2]
    elif x[0] % x[2] != 0:
        a = (x[0] // x[2]) + 1
        
    if x[1] < x[3]:
        b = 1
    elif x[1] % x[3] == 0:
        b = x[1] // x[3]
    elif x[1] % x[3] != 0:
        b = (x[1] // x[3]) + 1
        
    if a + b <= x[4]:
        print(a , b)
    else:
        print(-1)