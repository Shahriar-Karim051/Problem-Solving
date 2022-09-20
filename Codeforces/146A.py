

n = int(input())
a = input()
a = list(a)
s = 0
if a.count('4') + a.count('7') != n:
    print('NO')
else:
    for i in range(n // 2):
        s += int(a[i])
    for i in range(n // 2 , n):
        s -= int(a[i])
    print('YES' if s == 0 else 'NO')
    
   
    