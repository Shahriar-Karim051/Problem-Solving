
n = int(input())

x = [int(x) for x in input().split()]
ns = n - x[0]
if ns > n - 1:
   ns -= n
for i in range(n):
    if i % 2 == 0:
        ans = (n - x[i]) + i
        if ans > n - 1:
            ans -= n
    else:
        ans = x[i] - i
        if ans < 0:
            ans += n
    if ns != ans:
        print('NO')
        exit()
    
print('YES')
            
        