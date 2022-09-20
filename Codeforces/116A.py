
x = int(input())

s = 0

l = []

for i in range(x):
    a , b = input().split()
    a = int(a)
    b = int(b)
    s = s - a
    s = s + b
    l.append(s)
    
l.sort()

print(l[len(l) - 1])