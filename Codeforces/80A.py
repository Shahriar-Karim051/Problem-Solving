

a , b = input().split()

a = int(a) + 1
b = int(b)

l = [2 , 3 , 5 , 7]

if b not in l:
    if b % 2 == 0 or b % 3 == 0 or b % 5 == 0 or b % 7 == 0:
        print('NO')
        exit()
          

        
while a < b:
    if a in l:
        print('NO')
        exit()
    if a % 2 != 0 and a % 3 != 0 and a % 5 != 0 and a % 7 != 0:
        print('NO')
        exit()
            
    a = a + 1
    
print('YES')

