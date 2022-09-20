
x = int(input())


for i in range(x):
    z = int(input())
    if z == 0 or z == 1:
        print(0)
    else:
        print(z - ((z // 2) + 1))
        
    
