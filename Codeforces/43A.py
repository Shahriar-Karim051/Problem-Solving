
n = int(input())
l1 = []

l2 = []

a = input()
l1.append(a)

for i in range(n - 1):
    a = input()
    if a not in l1:
        l2.append(a)
    else:
        l1.append(a)
        
        
if len(l1) > len(l2):
    print(str(l1[0]))
else:
    print(str(l2[0]))

