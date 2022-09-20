
n = int(input())

if n % 2 == 0:
    a = n // 2 - 1 
    b = n // 2 + 1
    if a % 2 == 0 and b % 2 == 0:
        print(a - 1 , b + 1)
    else:
        print(a , b)
else:
    print(n // 2 , n - n // 2)