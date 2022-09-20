

n , c = map(int , input().split())

x = [int(x) for x in input().split()]
cnt = 0
for i in range(len(x) - 1):
    if x[i + 1] - x[i] <= c:
        cnt += 1
    else:
        cnt = 0
    
print(cnt + 1)