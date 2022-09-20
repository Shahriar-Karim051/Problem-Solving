
n = input()

n = int(n , 2)
cnt = 0
i = 0
while 1:
    if pow(4 , i) < n:
        cnt += 1
        i += 1
    else:
        break
    
print(cnt)