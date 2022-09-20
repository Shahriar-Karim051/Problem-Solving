

for i in range(int(input())):
    a = input()
    a = list(a)
    cnt = len(set(a))
    if cnt == 1:
        print(-1)
    else:
        a.sort()
        for j in a:
            print(str(j) , end = '')
            
    print()
    
        
    

