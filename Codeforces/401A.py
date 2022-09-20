import math
n , x = map(int , input().split())

p = [int(p) for p in input().split()]

print(math.ceil(abs(sum(p)) / abs(x)))