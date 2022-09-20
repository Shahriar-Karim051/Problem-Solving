
while 1:
    a = int(input())
    r = ""
    if a == 0:
        break
    else:
        for i in range(1 , a + 1):
            r += str(i) + ' '
        print(r[:-1])
    