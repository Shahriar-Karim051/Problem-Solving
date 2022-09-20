

n = int(input())
x = [int(x) for x in input().split()]

cp = cn = 0
for i in x:
    if i > 0:
        cp += 1
    elif i < 0:
        cn += 1
        
if cp >= n / 2:
    print(1)
elif cn >= n / 2:
    print(-1)
else:
    print(0)
