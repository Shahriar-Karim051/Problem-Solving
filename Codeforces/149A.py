
n = int(input())
count = 0
x = [int(x) for x in input().split()]
x.sort(reverse = True)

if n == 0:
    print(0)
elif sum(x) < n:
    print(-1)
else:
    for i in x:
        n = n - i
        count = count + 1
        if n <= 0:
            print(count)
            break
            