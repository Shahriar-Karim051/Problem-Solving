a , b = input().split()
a = int(a)
for i in range(a):
    x = input()
    if i % 2 == 0:
        d = 0
    else:
        d = 1
        
    for j in range(len(x)):
        if x[j] == '.':
            if d % 2 == 0:
                print('B' , end = '')
                d = d + 1
            else:
                print('W' , end = '')
                d = d + 1
        elif x[j] == '-':
            print('-' , end = '')
            d = d + 1
    print()
            