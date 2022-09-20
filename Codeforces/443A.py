
x = input()
if len(set(x)) < 3:
    print(0)
elif len(set(x)) == 3:
    print(1)
else:
    print(len(set(x)) - 4)