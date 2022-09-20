
n = int(input())

for i in range(n):
    x = [float(x) for x in input().split()]
    avg = ((x[0] * 2) + (x[1] * 3) + (x[2] * 5)) / 10
    print('%.1f'%avg)