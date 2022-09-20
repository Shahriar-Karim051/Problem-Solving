
for i in range(int(input())):
    l = []
    for j in range(int(input())):
        x = input()
        x = list(x)
        l.append((x))
    ans = 0
    for j in range(len(l) - 1):
        for k in range(len(l) - 1):
            if l[j][k] == '1':
                if l[j][k + 1] == '0' and l[j + 1][k] == '0':
                    ans = 1
                    break
    if ans == 0:
        print('YES')
    else:
        print('NO')
                
            
        