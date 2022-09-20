

x = [int(x) for x in input().split()]

if x[0] == 1:
    a = 4.0 * x[1]
    print("Total: R$ " + '%.2f'%a)
elif x[0] == 2:
    a = 4.5 * x[1]
    print("Total: R$ " + '%.2f'%a)
elif x[0] == 3:
    a = 5.0 * x[1]
    print("Total: R$ " + '%.2f'%a)
elif x[0] == 4:
    a = 2.0 * x[1]
    print("Total: R$ " + '%.2f'%a)
elif x[0] == 5:
    a = 1.5 * x[1]
    print("Total: R$ " + '%.2f'%a)