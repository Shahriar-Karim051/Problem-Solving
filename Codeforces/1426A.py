
for i in range(int(input())):
    n , x = map(int , input().split())
    if n <= 2:
        print(1)
    else:
        p = 2
        for j in range(2 , n):
            p += x
            if n <= p:
                print(j)
                break