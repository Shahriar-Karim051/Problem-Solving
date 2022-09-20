
x = int(input())
count = 0
for i in range(x):
    a , b = input().split()
    a = int(a)
    b = int(b)
    if b - a >= 2:
        count += 1
        
print(count)