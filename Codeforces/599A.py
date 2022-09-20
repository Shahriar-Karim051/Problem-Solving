
x = [int(x) for x in input().split()]

a = x[0] + x[1] + x[2]

b = 2 * x[0] + 2 * x[1]

c = 2 * min(x[0] , x[1]) + 2 * x[2]

print(min(a , b , c))