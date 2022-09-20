
a = input()

s = 0

while 1:
    for i in a:
        s = s + int(i)
    if s % 4 == 0:
        print(a)
        break
    else:
        a = int(a)
        a = a + 1
        a = str(a)
        s = 0
        