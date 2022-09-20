import math
a , b = input().split()
a = int(a)
b = int(b)

red = math.ceil((2 * a) / b)
green = math.ceil((5 * a) / b)
blue = math.ceil((8 * a) / b)

print(red + green + blue)