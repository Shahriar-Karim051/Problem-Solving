

n = int(input())

x = [int(x) for x in input().split()]

if x.count(0) == 0:
    print(len(set(x)))
else:
    print(len(set(x)) - 1)