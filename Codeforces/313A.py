
a = input()

if a[0] != '-':
    print(a)
else:
    if int(a[-1]) > int(a[-2]):
        if int(a[:-1]) == 0:
            print(0)
        else:
            print(a[:-1])
    else:
        if int(a[:-2] + a[-1]) == 0:
            print(0)
        else:
            print(a[:-2] + a[-1])