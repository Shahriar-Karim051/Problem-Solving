
n = int(input())

if n % 2 != 0:
    n = n - 1
    a = n // 2
    b = n - a
    while a % 3 == 0 or b % 3 == 0:
        a = a + 1
        b = b - 1
    print(1 , a , b)
else:
    n = n - 2
    a = n // 2
    b = n - a
    while a % 3 == 0 or b % 3 == 0:
        a = a + 1
        b = b - 1
    print(2 , a , b)
    