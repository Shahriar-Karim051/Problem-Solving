
x , y = input().split()

x = int(x)

y = int(y)

b = x
for i in range(1 , 10):
    a = b % 10
    #print(a)
    if a == 0:
        print(i)
        break
    elif a == y:
        print(i)
        break
    else:
        b = x * (i + 1)
        