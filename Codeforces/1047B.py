

n = int(input())
x , y = map(int , input().split())

mx = x + y

for i in range(n - 1):
    x , y = map(int , input().split())
    mx = max(mx , x + y)
    
print(mx)