
n = int(input())
m = int(input())
l = []
cnt = 0
for i in range(n):
    l.append(int(input()))
    
l.sort(reverse = True)

for i in l:
    m = m - i
    cnt += 1
    if m <= 0:
        print(cnt)
        break