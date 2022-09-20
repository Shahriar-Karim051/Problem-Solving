
n , d = map(int , input().split())
mx = 0
cnt = 0
for i in range(d):
    x = input()
    if x.count('0') > 0:
        cnt += 1
    else:
        mx = max(mx , cnt)
        cnt = 0
mx = max(mx , cnt)       
print(mx)
    