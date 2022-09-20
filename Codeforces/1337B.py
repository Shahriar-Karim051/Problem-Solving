
n = int(input())

for i in range(n):
    x = [int(x) for x in input().split()]
    if x[0] <= (10 * x[2]):
        print("YES")
    else:
        for j in range(x[1]):
            x[0] = (x[0] // 2) + 10
        x[0] = x[0] - (10 * x[2])
        if x[0] <= 0:
            print("YES")
        else:
            print("NO")
        
        
    
    
    
