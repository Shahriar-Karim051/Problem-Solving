
n = int(input())

r = [int(r) for r in input().split()]
b = [int(b) for b in input().split()]

cntr = cntb = 0

for i in range(n):
    if r[i] == 1 and b[i] == 0:
        cntr += 1
        #print(cntr)
    elif r[i] == 0 and b[i] == 1:
        cntb += 1
        #print(cntb)
        
if cntr == n and cntb == n:
    print(-1)
elif cntr == 0:
    print(-1)
elif cntr > cntb:
    print(1)
else:
    print((cntb // cntr) + 1)