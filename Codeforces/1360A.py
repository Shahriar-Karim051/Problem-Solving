
for i in range(int(input())):
    n , m = map(int , input().split())
    if n == m:
        print(pow(n + m , 2))
    else:
        a = max(m , n)
        b = min(m , n)
        if a % b == 0:
            print(pow(a , 2))
        else:
            print(max(pow(a , 2) ,pow(2 * b , 2)))