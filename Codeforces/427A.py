n = int(input())

x = [int(x) for x in input().split()]

a = cnt = 0

for i in x:
    if i == -1:
        a = a - 1
    else:
        a = a + i
    if a < 0:
        cnt = cnt + 1
        a = 0
        
print(cnt)