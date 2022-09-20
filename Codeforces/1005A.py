
n = input()

x = [int(x) for x in input().split()]
count = 1
best = -1
l = []
for i in x:
    if i > best:
        best = i
    else:
        l.append(best)
        best = i
        count = count + 1
l.append(x[-1])        
print(count)

for j in l:
    print(str(j) , end = ' ')