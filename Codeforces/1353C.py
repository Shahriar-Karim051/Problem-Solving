
from math import sqrt, ceil

for i in range(int(input())):
    a = int(input())
    if a == 1:
        print(0)
    else:
        a = (pow(a , 2) - 1) // 4
        for i in range(ceil(sqrt(a)), 0, -1):
            if a % i == 0:
                n = min(i, int(a / i))
                break
        print(int(8 * ((n * (n + 1) * (2 * n + 1)) / 6)))