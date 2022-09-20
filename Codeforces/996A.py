
x = int(input())

a = [100,20,10,5,1]

count = 0



for i in a:
    d = x // i
    count = count + d
    x = x % i
        
    
        
print(count)