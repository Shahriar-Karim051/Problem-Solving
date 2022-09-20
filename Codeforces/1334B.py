
for i in range(int(input())):
    a , b = map(int , input().split())
    x = [float(x) for x in input().split()]
    x.sort(reverse = True)
    c = 0
    if x[0] < b:
        print(c)
        continue
    elif x[-1] >= b:
        print(a)
        continue
    for j in range(a):
        if sum(x[ : j + 1]) / (j + 1) >= b:
            c = j + 1
        else:
            break
    print(c)
            
