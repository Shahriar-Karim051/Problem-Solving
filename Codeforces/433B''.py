# -*- coding: utf-8 -*-

n = int(input())
v = list(map(int, input().split()))
u = sorted(v)
dv, du = [0] * (n + 1), [0] * (n + 1)
ans = list()

for i in range(1, n + 1):
    dv[i] = dv[i-1] + v[i-1]
    print(dv[i])
    du[i] = du[i-1] + u[i-1]

for i in range(int(input())):
    (t, l, r) = map(int, input().split())
    d = dv if t == 1 else du
    ans.append(str(d[r] - d[l-1]))
    print(ans)

print('\n'.join(ans))