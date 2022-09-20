

from collections import Counter

n , k = map(int , input().split())

s = input()
s = list(s)

cnt = Counter(s)
r = 0
for i in cnt:
    if cnt[i] > k:
        r = 1
        break
    
print('YES' if r == 0 else 'NO')
    