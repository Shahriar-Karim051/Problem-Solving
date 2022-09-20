
m , n = map(int , input().split())
mn = 200
for i in range(m):
    a , b = map(int , input().split())
    if mn > a / b:
        mn = a / b
        
print(n * mn)
    
