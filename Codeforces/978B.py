
b = input()
a = input()
c = cnt = 0
for i in range(len(a)):
    if a[i] == 'x':
        c += 1
    else:
        if c > 2:
            cnt = cnt + c - 2
            c = 0
        else:
            c = 0
    
if c > 2:
    cnt = cnt + c - 2
   
print(cnt)