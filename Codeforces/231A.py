

x = int(input())
sum = 0
count = 0
for i in range(x):
    a = [int(a) for a in input().split()] 
    for j in range(len(a)):
        a[j] = int(a[j])
        sum = sum + a[j]
    if sum >= 2:
        count = count + 1
        sum = 0
    else:
        sum = 0
        
        
print(count)
        