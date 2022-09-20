
n = int(input())
a = [int(a) for a in input().split()]
a.sort()
s = 0
p = -1
for i in range(n // 2):
    s += pow((a[i] + a[p]) , 2)
    p -= 1
    
print(s)
    