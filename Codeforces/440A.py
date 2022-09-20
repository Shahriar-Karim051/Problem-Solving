

n = int(input())
b = [int(b) for b in input().split()]
l = []
for i in range(1 , n + 1):
    l.append(i)
    
print(*(set(l) ^ set(b)))