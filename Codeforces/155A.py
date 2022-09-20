
n = input()

x = [int(x) for x in input().split()]

max = x[0]
min = x[0]
count = 0
for i in x:
    if i > max:
        count = count + 1
        max = i
    elif i < min:
        count = count + 1
        min = i
        
        
print(count)