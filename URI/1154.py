s = count = 0
while 1:
    a = int(input())
    if a < 0:
        break
    else:
        s = s + a
        count = count + 1
        
        
avg = s / count

print('%.2f'%avg)