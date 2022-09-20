

n = int(input())

r = ""

s = a = 0
b = 1
if n == 0:
    print('0')
elif n == 1:
    print('0')
elif n == 2:
    print('0 1')
else:
    r += '0 1 '
    for i in range(n - 2):
        s = a + b
        a = b
        b = s
        r += str(s) + ' '
    
print(r[:-1])
    