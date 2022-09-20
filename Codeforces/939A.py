
a = int(input())

x = [int(x) for x in input().split()]


if a < 3:
    print('NO')
    exit()
for i in range(a):
    if x[x[x[i] - 1] - 1] - 1 == i:
        print('YES')
        exit()
    
print('NO')