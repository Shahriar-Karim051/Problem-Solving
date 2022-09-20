
a , b , c = map(int , input().split())

x = [int(x) for x in input().split()]
cnt = waste = 0
for i in x:
    if i <= b:
        waste = waste + i
    
    if waste > c:
        cnt += 1
        waste = 0


        
print(cnt)
        