

for i in range(int(input())):
    n = int(input())
    for j in range(2 , 31):
        if n % (pow(2 , j) - 1) == 0:
            print(n // (pow(2 , j) - 1))
            break