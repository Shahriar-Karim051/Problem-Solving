
a , b = input().split()

a = int(a)
b = int(b)
c = b
if a == 1 and b <= 9:
    print(b)
elif a == 1 and b > 9:
    print(-1)
elif a == len(str(b)):
    print(b)
else:
    for i in range(a):
        c = c * 10
        #print(c)
        if len(str(c)) == a:
            print(c)
            exit()
        
    
    

        
    
        
