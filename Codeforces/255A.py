
n = int(input())

x = [int(x) for x in input().split()]

bi = ba = ch = 0

for i in range(n):
    if (i + 1) % 3 == 1:
        ch = ch + x[i]
    elif (i + 1) % 3 == 2:
        bi = bi + x[i]
    else:
        ba = ba + x[i]
        
if max(bi , ba , ch) == bi:
    print('biceps')
elif max(bi , ba , ch) == ba:
    print('back')
else:
    print('chest')