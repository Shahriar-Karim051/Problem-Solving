
n, m = input().split()

m = int(m)
n = int(n)

pos = 0
count = 0
x = [int(x) for x in input().split()]

for i in x:
    if i > pos:
        count = count + (i - pos)
        pos = i
    elif i < pos:
        count = count + i + (n - pos)
        pos = i
        
print(count - 1)