
n , m = map(int , input().split())

r = m % ((n * (n + 1)) // 2)

if r == 0:
    print(0)
else:
    for i in range(1 , n + 1):
        if i <= r:
            r -= i
        else:
            print(r)
            break