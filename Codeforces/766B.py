
n = int(input())

x = [int(x) for x in input().split()]

x.sort(reverse = True)

for i in range(n):
    for j in range(i + 1 , n - 1):
        if x[i] + x[j] > x[j + 1] and x[j] + x[j + 1] > x[i] and x[i] + x[j + 1] > x[j]:
            print('YES')
            exit()

print('NO')