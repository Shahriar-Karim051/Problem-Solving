
a = input()

x = [int(x) for x in input().split()]

x.sort()

if sum(x) % 2 == 0:
    print(sum(x))
else:
    for i in x:
        if i % 2 != 0:
            print(sum(x) - i)
            break