

n = int(input())

for i in range(n):
    a , b = input().split()
    a = int(a)
    b = int(b)
    x = [int(x) for x in input().split()]
    if sum(x) > b:
        print(b)
    else:
        print(sum(x))