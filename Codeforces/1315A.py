

for i in range(int(input())):
    x = [int(x) for x in input().split()]
    print(max(max(x[2] , (x[0] - 1 - x[2])) * x[1] , max(x[3] , x[1] - 1 - x[3]) * x[0]))