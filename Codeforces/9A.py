
x = [int(x) for x in input().split()]
x.sort()


if x[-1] == 1:
    print("1/1")
elif x[-1] == 2:
    print("5/6")
elif x[-1] == 3:
    print("2/3")
elif x[-1] == 4:
    print("1/2")
elif x[-1] == 5:
    print("1/3")
else:
    print("1/6")
