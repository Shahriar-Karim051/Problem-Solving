

for i in range(int(input())):
    a = input()
    x = [int(x) for x in input().split()]
    cnt1 = cnt2 = 0
    for i in range(len(x)):
        if i % 2 == 0:
            if x[i] % 2 != 0:
                cnt1 += 1
        else:
            if x[i] % 2 == 0:
                cnt2 += 1
    print(-1 if cnt1 != cnt2 else cnt1)