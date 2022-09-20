
a = int(input())

x = [int(x) for x in input().split()]
x.sort()

c = 0

for i in range(1 , a):
    if x[i] == x[i - 1]:
        x[i] = x[i] + 1
        c += 1
        
    elif x[i] < x[i - 1]: 
        b = x[i - 1] - x[i]
        x[i] = x[i] + b + 1
        c = c + b + 1
    
print(c)