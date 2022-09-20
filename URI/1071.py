
x = int(input())
y = int(input())

count = 0

for i in range(min(x , y) + 1 , max(x , y)):
    #print(i)
    if i % 2 != 0:
        count = count + i
        
print(count)