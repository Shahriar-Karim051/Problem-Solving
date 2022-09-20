
n = int(input())
count = 0
for i in range(n):
    x = [int(x) for x in input().split()]
    
    if x[0] == x[1]:
        count = count + 1
        
        
if count == n:
    print("Poor Alex")
else:
    print("Happy Alex")




    