x = input()
x = int(x)
a = [4 , 7 , 44 , 47 , 74 , 77 , 444 , 447 , 474 , 477 , 744 , 747 , 777]
count = 0
if x in a:
    print("YES")
else:
    for i in range(len(a)):
        if x % a[i] == 0:
            count +=1
    if count == 0:
        print("NO")
    else:
        print("YES")
    
    
   
    
   
