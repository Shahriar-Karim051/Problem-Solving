
n , x = input().split()
n = int(n)
x = int(x)
count = 0
for i in range(n):
    a , b = input().split()
    b = int(b)
    if a == '+':
        x = x + b
    else:
        if x >= b:
            x = x - b
        else:
            count = count + 1
            
print(x , count)
        
    
    