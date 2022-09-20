
a = int(input())

a = a + 1

a = str(a)


for i in range(8001):
    s = set(a)
    if len(s) == 4:
        print(a)
        break
    else:
        a = int(a)
        a = a + 1
        a = str(a)