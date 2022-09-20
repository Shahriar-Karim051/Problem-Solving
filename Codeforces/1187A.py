

for i in range(int(input())):
    x = [int(x) for x in input().split()]
    print(max((x[0] - x[1]) , (x[0] - x[2])) + 1)