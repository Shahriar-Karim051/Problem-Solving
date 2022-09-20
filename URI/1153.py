

n = int(input())

s = 1

if n == 0:
    print(1)
else:
    for i in range(n):
        s = s * (n - i)
    
print(s)