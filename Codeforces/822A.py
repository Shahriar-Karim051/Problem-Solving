import math

a , b = input().split()

a = int(a)
b = int(b)

print(math.factorial(min(a,b)))