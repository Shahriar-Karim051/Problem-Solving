
for i in range(int(input())):
    n = int(input())
    b = [int(b) for b in input().split()]
    b.sort()
    g = [int(g) for g in input().split()]
    g.sort()
    c = 0
    if b[0] < g[0]:
        for j in range(1 , n):
            if b[j] < g[j - 1]:
                c = 1
                break
            if g[j] < b[j]:
                c = 1
                break
    elif b[0] > g[0]:
        for j in range(1 , n):
            if g[j] < b[j - 1]:
                c = 1
                break
            if b[j] < g[j]:
                c = 1 
                break
    elif b[0] == g[0]:
        d = e = 0
        for j in range(n - 1):
            if b[j] > g[j + 1]:
                d = 1
                break
            if g[j + 1] > b[j + 1]:
                d = 1
                break
        for k in range(n - 1):
            if g[k] > b[k + 1]:
                e = 1
                break
            if b[k + 1] > g[k + 1]:
                e = 1
                break
        if d == 0 or e == 0:
            c == 0
        else:
            c == 1
    
        
    if c == 1:
        print('NO')
    else:
        print('YES')
            