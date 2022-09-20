
n = int(input())
prime = []


for i in range(2 , n + 1):
    r = 0
    for j in range(2 , i):
        if i % j == 0 and i != j:
            r += 1
    if r == 0:
        prime.append(i)
        
cnt = 0

for i in range(2 , n + 1):
    p = 0
    for j in range(2 , i + 1):
        if i % j == 0 and j in prime:
            p += 1
    if p == 2:
        cnt += 1
            
            
        
print(cnt)
    