

n = int(input())


for i in range(n):
    a = input()
    b = [int(b) for b in input().split()]
    c = 0
    for i in b:
        if i == 0:
            c = c + 1
    if sum(b) + c == 0:
        print(c + 1)
    else:
        print(c)