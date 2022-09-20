
for i in range(int(input())):
    s = int(input())
    c = s // 10
    x = c + s % 10
    s += c
    while x >= 10:
        a = x // 10
        b = a + x % 10
        s += a
        x = b
        
    print(s)