
n = int(input())
for i in range(2 , n):
    if n % i == 0:
        a = n // i
        print(str(i) + str(a))
        exit()