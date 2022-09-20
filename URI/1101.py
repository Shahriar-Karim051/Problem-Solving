

while 1:
    a , b = input().split()
    a = int(a)
    b = int(b)
    if a == 0 or b == 0:
        break
    s = 0
    for i in range(min(a , b) , max(a , b) + 1):
        print(i , end = ' ')
        s = s + i
    print('Sum=' + str(s))
    
    