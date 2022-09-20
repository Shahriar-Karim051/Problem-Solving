

for i in range(int(input())):
    n = int(input())
    a = [int(a) for a in input().split()]
    for j in range(n - 1):
        if a[j] > a[j + 1]:
            cnt = 0
        else:
            cnt = 1
            break
            
    print('YES' if cnt == 1 else 'NO')
        
        