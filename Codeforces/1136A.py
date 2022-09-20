
l = []
for i in range(int(input())):
    a , b = map(int , input().split())
    l.append(b)
    
n = int(input())

cnt = 0
for j in l:
    if j < n:
        cnt = cnt + 1
        
print(len(l) - cnt)