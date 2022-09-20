
a , b = input().split()



b = int(b)

#print(a[0])
for i in range(b):
    z = len(a) - 1
    if int(a[z]) == 0:
        a = int(a)
        a = a // 10
    else:
        a = int(a)
        a -= 1
    a = str(a)
    
    
print(a)