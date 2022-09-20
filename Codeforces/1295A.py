
n = int(input())

for i in range(n):
    a = int(input())
    r = ''
    if a % 2 == 0:
        for j in range(a // 2):
            r += '1'
    else:
        r += '7'
        for j in range((a - 3) // 2):
            r += '1'
    print(r)