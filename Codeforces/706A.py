import math
a , b = map(int , input().split())

n = int(input())

x = [int(x) for x in input().split()]

mn = math.sqrt(pow(a - x[0], 2) + pow(b - x[1], 2)) / x[2]


for i in range(n - 1):
    x = [int(x) for x in input().split()]
    mn = min(mn , math.sqrt(pow(a - x[0], 2) + pow(b - x[1], 2)) / x[2])
    
print(mn)