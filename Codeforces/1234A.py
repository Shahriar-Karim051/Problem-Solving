
n = int(input())

for i in range(n):
    a = int(input())
    x = [int(x) for x in input().split()]
    if sum(x) % a == 0:
        print(sum(x) // a)
    else:
        print((sum (x) // a) + 1)