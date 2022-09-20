
n = int(input())

x = [int(x) for x in input().split()]
l = []
avg = sum(x) // (n // 2)

for i in range(n):
    for j in range(n):
        if x[i] + x[j] == avg:
            if i not in l and j not in l and i != j:
                l.append(i)
                l.append(j)
                print(i + 1 , j + 1)