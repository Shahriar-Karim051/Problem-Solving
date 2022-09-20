
n = int(input())
x = [int(x) for x in input().split()]
l = []
r = 0

for i in range(n+n):
    if x[i] not in l:
        l.append(x[i])
        r += 1
        #print(i)
    if r == n:
        print(n-((i+1)%n))
        break
    
        
