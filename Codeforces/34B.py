
m , n = input().split()

n = int(n)

x = [int(x) for x in input().split()]

x.sort()
s = 0
a = 0
for i in range(n):
    s = s + (x[i] * -1)
    if s > a:
        a = s
    else:
        print(a)
        exit()
    
print(s)