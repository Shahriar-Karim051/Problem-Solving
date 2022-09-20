
for i in range(int(input())):
    a = int(input())
    l = []
    if a % 4 != 0:
        print('NO')
    else:
        print('YES')
        for j in range(2 , a + 1 , 2):
            l.append(j)
        for k in range(1 , a - 1 , 2):
            l.append(k)
        l.append(a - 1 + (a // 2))
        
        for m in l:
            print(str(m) , end = ' ')