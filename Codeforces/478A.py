
x = [int(x) for x in input().split()]

if sum(x) == 0:
    print(-1)
elif sum(x) % 5 == 0:
    print(sum(x) // 5)
else:
    print(-1)