

r , c = map(int , input().split())

row = [0]*r
col = [0]*c
cnt = 0
for i in range(r):
    a = list(input())
    for j in range(c):
        if a[j] == 'S':
            row[i] = 1
            col[j] = 1
    r1 = row.count(1)
    c1 = col.count(1)
    
print((r * c) - (r1 * c1))
