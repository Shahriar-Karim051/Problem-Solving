
n = int(input())

x = [int(x) for x in input().split()]
x.extend(x)
mx = cnt = 0
for i in range(2 * n):
    if x[i] == 0:
        for j in range(i + 1 , 2 * n):
            if x[j] == 1:
                cnt = cnt + 1
            else:
                mx = max(mx , cnt)
                cnt = 0
                break
            
print(mx)