import math
x = [int(x) for x in input().split()]
count = 0
while(x[-1] > 0):
    x[-1] = x[-1] - math.gcd(x[0] , x[-1])
    count = count + 1
    if x[-1] != 0:
        x[-1] = x[-1] - math.gcd(x[1] , x[-1])
        count = count + 1
        
        
if count % 2 == 0:
    print(1)
else:
    print(0)
    
