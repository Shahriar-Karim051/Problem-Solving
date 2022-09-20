

for i in range(int(input())):
    n = int(input())
    s = input()

    c = 0
    cnt = 0
    for j in s:
        if j == ')':
            if c == 0:
                cnt += 1
            else:
                c -= 1
        else:
            c += 1
        
    print(cnt)


    
    
    