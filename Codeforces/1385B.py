

for i in range(int(input())):
    n = int(input())
    a = [int(a) for a in input().split()]
    l = []
    for j in a:
        if j not in l:
            l.append(j)
    print(*l)