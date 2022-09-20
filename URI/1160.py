n = int(input())

for i in range(n):
    x = [float(x) for x in input().split()]
    count = 0
    while(x[0] <= x[1]):
        x[0] = x[0] + int(x[0] * (x[2] / 100))
        x[0] = int(x[0])
        x[1] = x[1] + int(x[1] * (x[3] / 100))
        x[1] = int(x[1])
        count = count + 1
        if count > 100:
            break
    
    if count > 100:
        print('Mais de 1 seculo.')
    else:
        print(count , 'anos')
            