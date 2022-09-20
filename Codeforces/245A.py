
cnt1 = cnt2 = 0
for i in range(int(input())):
    x = [int(x) for x in input().split()]
    if x[0] == 1:
        cnt1 = cnt1 + x[1] - x[2]
    else:
        cnt2 = cnt2 + x[1] - x[2]
        
print('LIVE' if cnt1 >= 0 else 'DEAD')
print('LIVE' if cnt2 >= 0 else 'DEAD')