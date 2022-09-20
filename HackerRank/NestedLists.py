a = []
grade = []
for i in range(int(input())):
    l = []
    n = input()
    g = float(input())
    grade.append(g)
    l.append(n)
    l.append(g)
    a.append(l)
    
y = sorted(set(grade))
print(y)
a.sort(key = lambda x: x[1])
b = []
for i in range(len(a)):
    if y[1] == a[i][1]:
        b.append(a[i][0])

b.sort()

for i in b:
    print(str(i))
    