l = []
a = int(input())
l.append(a)
b = int(input())
l.append(b)
c = int(input())
l.append(c)
l.sort()
print(min((l[0] - (l[1] * l[2])) , (l[0] - l[1] - l[2])))
