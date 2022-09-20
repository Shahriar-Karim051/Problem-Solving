

for i in range(int(input())):
    a = input()
    cnt = 1
    if len(a) == 1:
        print('YES')
    elif len(set(a)) != len(a):
        print('NO')
    else:
        a = list(a)
        a.sort()
        #print(a)
        for j in range(len(a) - 1):
            if ord(a[j]) - ord(a[j + 1]) != -1:
                cnt = 0
                    
                    
        print('YES' if cnt == 1 else 'NO')