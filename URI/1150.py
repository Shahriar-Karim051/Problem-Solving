
a = int(input())

while 1:
    b = int(input())
    if b > a:
        break
s = count = 0   
for i in range(a , b):
    s = s + i
    count = count + 1
    if s >= b:
        break
    
print(count)