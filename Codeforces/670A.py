

n = int(input())
m = n
offmin = offmax = 0
while 1:
    if n <= 2:
        offmax += n
        break
    else:
        offmax += 2
        n -= 2
    if n <= 5:
        break
    else:
        n -= 5
    
while 1:
    if m <= 5:
        break
    else:
        m -= 5
    if m <= 2:
        offmin += m
        break
    else:
        offmin += 2
        m -= 2

print(offmin , offmax)
    
    