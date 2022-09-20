

for i in range(int(input())):
    n = int(input())
    x = [int(x) for x in input().split()]
    ans = 0
    if n == 1:
        print('YES')
    else:
        for j in range(len(x) - 1):
            if abs(x[j] - x[j + 1]) % 2 != 0:
                ans = 1
        print('NO' if ans == 1 else 'YES')
        