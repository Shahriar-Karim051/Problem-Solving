
a , b = input().split()

a = int(a)
b = int(b)
count = 0
while a <= b:
    a = 3 * a
    b = 2 * b
    count += 1
    
print(count)