

for i in range(int(input())):
    n , k = map(int , input().split())
    if n % 2 == 0:
        print(n + (2 * k))
    else:
        for j in range(3 , n + 1):
            if n % j == 0:
                print(n + j + (2 * (k - 1)))
                break
            