
n = int(input())

for i in range(n):
    a = int(input())
    count = 0
    if a == 1 or a == 2 or 1 == 3:
        print(a , 'eh primo')
    else:
        for j in range(2 , a // 2 + 1):
            if a % j == 0:
               count = count + 1
               break
        if count == 1:
           print(a , 'nao eh primo')
        else:
            print(a , 'eh primo')
    
    