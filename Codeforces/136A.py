
n = int(input())
x = [int(x) for x in input().split()]

for i in range(1 , n + 1):
    print(x.index(i) + 1 , end = ' ')