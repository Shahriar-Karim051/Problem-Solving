

n = int(input())

for i in range(n):
    a = [int(a) for a in input().split()]
    b = [int(b) for b in input().split()]
    if a[0] >= 2 * (a[1] + a[2]):
        print(a[1] * b[0] + a[2] * b[1]) 
    elif max(b[0] , b[1]) == b[0]:
        if a[0] <= 2 * a[1]:
            print((a[0] // 2) * b[0])
        else:
            print((a[1] * b[0]) + (((a[0] - 2 * a[1]) // 2) * b[1]))
    elif max(b[0] , b[1]) == b[1]:
        if a[0] <= 2 * a[2]:
            print((a[0] // 2) * b[1])
        else:
            print((a[2] * b[1]) + (((a[0] - 2 * a[2]) // 2) * b[0]))
            