
n = int(input())

a = [int(a) for a in input().split()]

cnt1 = cnt0 = 0
mx = -1

for i in a:
    if i == 0:
        cnt0 += 1
        mx = max(mx , cnt0)
    else:
        cnt1 += 1
        if cnt0 != 0:
            cnt0 -= 1

print(cnt1 + mx)