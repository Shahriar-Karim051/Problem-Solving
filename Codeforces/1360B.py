
for i in range(int(input())):
    a = input()
    x = [int(x) for x in input().split()]
    x.sort(reverse = True)
    mn = x[0] - x[1]
    for j in range(len(x) - 1):
        if x[j] - x[j + 1] < mn:
            mn = x[j] - x[j + 1]
    print(mn)