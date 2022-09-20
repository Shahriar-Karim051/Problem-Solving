import re
a , y = input().split()

x = input()

y = int(y)



for j in range(y):
    x = re.sub("BG" , "GB" , x)
        
            
            
            
print(x)
    
    
