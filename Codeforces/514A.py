

a = input()

r = ''
if int(a[0]) > 4 and int(a[0]) <= 8:
    b = 9 - int(a[0])
    r += str(b)
else:
    r += a[0]
    
for i in range(1 , len(a)):
    if int(a[i]) > 4:
        b = 9 - int(a[i])
        r += str(b)
    else:
        r += a[i]
        
print(r)