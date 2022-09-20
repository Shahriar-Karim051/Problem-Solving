

t = int(input())

for i in range(t):
    a , b = input().split()
    a = int(a)
    b = int(b)
    if a % b == 0:
        print(0)
    else:
        if a > b:
            print((b * ((a // b) + 1)) - a)
        else:
            print(b -a)