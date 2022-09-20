
n = int(input())

x = [int(x) for x in input().split()]
x.sort()
a = len(set(x))
cnt = 0
if a <= 2:
    print(0)
else:
    for i in range(n):
        if x[i] == x[0] or x[i] == x[-1]:
            cnt += 1
            
    print(len(x) - cnt)