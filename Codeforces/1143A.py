

n = int(input())

x = [int(x) for x in input().split()]

z = x.count(0)
o = x.count(1)
cnt = 0
for i in range(n):
    if x[i] == 0:
        cnt += 1
        z -= 1
        if z == 0:
            print(cnt)
            break
    else:
        cnt += 1
        o -= 1
        if o == 0:
            print(cnt)
            break
