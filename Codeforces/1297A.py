

for i in range(int(input())):
    n = int(input())
    if n < 1000:
        print(n)
    elif n >= 1000 and n <= 999499:
        print(str((n + 500) // 1000) + 'K')
    else:
        print(str((n + 500000) // 1000000 ) + 'M')