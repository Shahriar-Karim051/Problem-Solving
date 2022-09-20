

for i in range(int(input())):
    n = int(input())
    a = [int(a) for a in input().split()]
    a.sort()
    step = 1
    cnt = 0
    for j in range(n - 2):
        if step < a[-2]:
            cnt += 1
            step += 1
        else:
            break
    print(cnt)