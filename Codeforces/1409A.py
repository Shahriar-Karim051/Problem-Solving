import math

for i in range(int(input())):
    a , b = map(int , input().split())
    c = abs(a - b)
    if c == 0:
        print(0)
    else:
        print(math.ceil(c / 10))