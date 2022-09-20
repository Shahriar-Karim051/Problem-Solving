
n = int(input())

for i in range(n):
    a = int(input())
    a = 360 % (180 - a)
    if a == 0:
        print("YES")
    else:
        print("NO")