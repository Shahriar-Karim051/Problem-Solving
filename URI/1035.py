
x = [int(x) for x in input().split()]


if x[1] > x[2] and x[3] > x[0] and x[2] + x[3] > x[1] + x[0] and x[2] > 0 and x[3] > 0 and x[0] % 2 == 0:
    print("Valores aceitos")
else:
    print("Valores nao aceitos")