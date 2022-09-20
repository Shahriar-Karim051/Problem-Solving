
n = input()

x = [int(x) for x in input().split()]


if x[-1] == 15:
    print('DOWN')
elif x[-1] == 0:
    print('UP')
elif len(x) <= 1:
    print(-1)
elif x[-2] < x[-1]:
    print('UP')
else:
    print('DOWN')