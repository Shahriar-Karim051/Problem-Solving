
a = int(input())
b = int(input())
c = int(input())
s = 0
while a >= 1 and b >= 2 and c >= 4:
    a = a - 1
    b = b - 2
    c = c - 4
    s = s + 7

print(s)