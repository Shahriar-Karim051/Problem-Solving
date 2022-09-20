

n = int(input())

x = input()
s = f = 0
for i in range(n - 1):
    if x[i] == 'S' and x[i + 1] == 'F':
        s = s + 1
    elif x[i] == 'F' and x[i + 1] == 'S':
        f = f + 1
        
if s > f:
    print('YES')
else:
    print('NO')