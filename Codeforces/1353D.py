

for i in range(int(input())):
    a = int(input())
    l = []
    if a == 1:
        print(1)
    elif a == 2:
        print('1 2')
    else:
        if a % 2 == 0:
            for j in range(3 , a , 2):
                l.append(j)
            l.append(1)
            for k in range(2 , a + 1 , 2):
                l.append(k)
        else:
            for j in range(2 , a , 2):
                l.append(j)
            l.append(1)
            for k in range(3 , a + 1 , 2):
                l.append(k)
        for m in l:
            print(str(m) , end = ' ')
    print()
                