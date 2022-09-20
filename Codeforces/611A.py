

n = input()
x = int(n[0])
a = x
i = 5
if n[1] != ' ':
    y = int(n[1])
    a = x * 10 + y
    i += 1
else:
    y = 0
    
if n[i] == 'w':
    if x == 5 or x == 6:
        print(53)
    else:
        print(52)
else:
    if a <= 29:
        print(12)
    elif a == 30:
        print(11)
    elif a == 31:
        print(7)
    
