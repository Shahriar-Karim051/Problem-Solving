import math
a = input()

cnt = 0
c = -1
for i in range(math.ceil(len(a) // 2)):
    if a[i] != a[c]:
        cnt = cnt + 1
    c = c - 1
    
            
if cnt == 1:
    print('YES')
elif cnt == 0 and len(a) % 2 == 1:
    print('YES')
else:
    print('NO')
    