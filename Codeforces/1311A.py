
n = int(input())

for i in range(n):
    a , b = input().split()
    a = int(a)
    b = int(b)
    if a == b:
        print(0)
    elif a > b:
        if a % 2 == b % 2 == 0 or a % 2 == b % 2 != 0 :
            print(1)
        else:
            print(2)
    elif a < b:
        if a % 2 == b % 2 == 0 or a % 2 == b % 2 != 0:
            print(2)
        else:
            print(1)