

n = int(input())

for i in range(n):
    s = 0
    x = [int(x) for x in input().split()]
    if x[0] % 2 == 0:
        a = x[0] + 1
    else:
        a = x[0]
    for i in range(x[1]):
        s = s + a
        a = a + 2
    print(s)