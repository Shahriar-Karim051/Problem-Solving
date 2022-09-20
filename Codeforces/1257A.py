
n = int(input())

for i in range(n):
    a = [int(a) for a in input().split()]
    b = a[0] - 1
    if abs(a[2] - a[3]) == b or abs(a[2] - a[3]) + a[1] >= b:
        print(b)
    else:
        print(abs(a[2] - a[3]) + a[1])
    
    
    