

n = int(input())

for i in range(n):
    a = int(input())
    s = (a * (a + 1)) // 2
    p = 1
    while p <= a:
        p = p * 2
        s = s - p
    print(s)