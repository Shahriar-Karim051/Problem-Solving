
n = int(input())

x = [int(x) for x in input().split()]
x.append(0)
p = q = cnt1 = cnt2 = best = 0
for i in range(n):
    if x[i] == 1:
        cnt1 += 1
        if x[i + 1] == 2:
            p = cnt1
            cnt1 = 0
    else:
        cnt2 += 1
        if x[i + 1] == 1:
            q = cnt2
            cnt2 = 0
    best = max(best , min(p , q))
    
    if x[i + 1] == 0:
        best = max(best , min(max(cnt1 , p) , max(cnt2 , q)))
    



print(best * 2)