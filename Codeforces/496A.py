

n = int(input())

a = [int(a) for a in input().split()]

mx = a[1] - a[0]

for i in range(1 , n - 1):
    mx = max(mx , a[i + 1] - a[i])
l = []    
l.append(max(mx , a[2] - a[0]))
for i in range(1 , n - 2):
    l.append(max(mx , a[i + 1] - a[i - 1]))
    
l.sort()

print(l[0])
    
