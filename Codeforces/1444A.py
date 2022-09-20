
for i in range(int(input())):
    p , q = map(int , input().split())
    n = p
    while n >= 1:
        if (p % n == 0):
            if (n % q != 0):
                print(n)
                break
        n -= 1