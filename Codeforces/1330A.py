

n = int(input())

for i in range(n):
    a , b = input().split()
    b = int(b)
    x = [int(x) for x in input().split()]
    c = 0
    for i in range(b):
        c = c + 1
        while c in x:
            c = c + 1
    while c + 1 in x:
        c = c + 1
    print(c)
            
            