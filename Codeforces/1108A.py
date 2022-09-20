

n = int(input())

for i in range(n):
    x = [int(x) for x in input().split()]
    if x[0] != x[2]:
        print(x[0] , x[2])
    elif x[0] != x[3]:
        print(x[0] , x[3])
    elif x[1] != x[3]:
        print(x[1] , x[3])
    elif x[1] != x[2]:
        print(x[1] , x[2])
        