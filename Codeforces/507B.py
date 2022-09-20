import math
x = [int(x) for x in input().split()]

a = math.ceil(math.sqrt((x[1] - x[3]) * (x[1] - x[3]) + (x[2] - x[4]) * (x[2] - x[4])) / (x[0] + x[0]))

print(a)