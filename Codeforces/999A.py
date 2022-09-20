

a , b = input().split()

a = int(a)
b = int(b)

x = [int(x) for x in input().split()]
cnt = 0
for i in x:
    if i <= b:
        cnt = cnt + 1
    else:
        break
    
x.reverse()

for j in x:
    if j <= b:
        cnt = cnt + 1
    else:
        break
    
if cnt > a:
    print(a)
else:
    print(cnt)