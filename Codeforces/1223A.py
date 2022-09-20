
n = int(input())

for i in range(n):
    a = int(input())
    if a <= 4:
        print(4 - a)
    elif a > 4 and a % 2 == 0:
        print(0)
    else:
        print(1)
    