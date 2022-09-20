import math
for i in range(int(input())):
    a = int(input())
    if a % 2 != 0:
        a = a - 1
    print(math.gcd(a , a // 2))