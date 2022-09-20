
a = int(input())

x = [int(x) for x in input().split()]

x.sort()

if a <= 2:
    print(0)
else:
    print(min(abs(x[0] - x[-2]) , abs(x[1] - x[-1])))