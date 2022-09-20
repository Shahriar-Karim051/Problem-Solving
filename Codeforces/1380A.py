

for i in range(int(input())):
    n = int(input())
    a = [int(a) for a in input().split()]
    c = 0
    for j in range(1 , len(a) - 1):
        if a[j] > a[j - 1] and a[j] > a[j + 1]:
            print('YES')
            print(j , j + 1 , j + 2)
            c = 1
            break
    if c == 0:
        print('NO')
        