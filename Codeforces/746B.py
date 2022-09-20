
a = int(input())
n = input()
l = list(n)
s = []

s.append(l[0])

if a % 2 != 0:
    for i in range(1 , a):
        if i % 2 == 0:
            s.append(l[i])
        else:
            s.insert(0 , l[i])
else:
    for i in range(1 , a):
        if i % 2 != 0:
            s.append(l[i])
        else:
            s.insert(0 , l[i])
            
for i in s:
    print(str(i) , end = '')