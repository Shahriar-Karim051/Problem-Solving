
for i in range(int(input())):
    a , b = input().split()
    for i in range(1 , int(b)):
        c = list(a)
        c.sort()
        if int(c[0]) * int(c[-1]) != 0:
            a = int(a) + int(c[0]) * int(c[-1])
            a = str(a)
        else:
            break
        
    print(a)