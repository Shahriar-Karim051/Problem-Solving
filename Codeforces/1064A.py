

x = [int(x) for x in input().split()]
x.sort()

print(max(0 , x[2] - (x[0] + x[1] - 1)))