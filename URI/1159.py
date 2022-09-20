
while 1:
    a = int(input())
    if a == 0:
        break
    elif a % 2 != 0:
        a = a + 1
    s = 0
    for i in range(5):
        
        s = s + a
        a = a + 2
    print(s)