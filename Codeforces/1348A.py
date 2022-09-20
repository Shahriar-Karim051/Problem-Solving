
n = int(input())

for i in range(n):
    a = int(input())
    b = a // 2
    c = pow(2 , a + 1) - 2 - (pow(2 , a) + pow(2 , b) - 2)
    print((pow(2 , a) + pow(2 , b) - 2) - c)