
a , b = input().split()
a = int(a)
b = int(b)
cnt = 0
while a and b:
    if a > b:
        if a >= 2:
            a = a - 2
            b = b - 1
            cnt = cnt + 1
        else:
            break
    else:
        if b >= 2:
            b = b - 2
            a = a - 1
            cnt = cnt + 1
        else:
            break
        
print(cnt)