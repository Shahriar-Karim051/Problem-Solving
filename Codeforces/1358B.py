

for i in range(int(input())):
    a = int(input())
    x = [int(x) for x in input().split()]
    x.sort(reverse = True)
    ans = 0
    for j in x:
        if j <= a:
            ans = a + 1
        else:
            a -= 1
    if ans == 0:
        print(1)
    else:
        print(ans)