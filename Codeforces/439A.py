

a , b = input().split()
a = int(a)
b = int(b)

x = [int(x) for x in input().split()]


if sum(x) + (a - 1) * 10 <= b:
    print((b - sum(x)) // 5)
else:
    print(-1)


    

 