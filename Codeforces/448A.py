
x = [int(x) for x in input().split()]

y = [int(y) for y in input().split()]

n = int(input())
if sum(x) > 0 and sum(x) < 5:
    s = 1
elif sum(x) % 5 == 0:
    s = (sum(x) // 5) 
else:
    s = (sum(x) // 5) + 1
   
if sum(y) > 0 and sum(y) < 10:
    s = s + 1    
elif sum(y) % 10 == 0:
    s = s + sum(y) // 10
else:
    s = s + 1 + sum(y) // 10
   
if s <= n:
    print("YES")
else:
    print("NO")