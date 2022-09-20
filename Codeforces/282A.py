
x = int(input())
count = 0
for i in range(x):
    a = input()
    if a[1] == '+':
        count = count + 1
    elif a[1] == '-':
        count = count - 1
        
    
print(count)