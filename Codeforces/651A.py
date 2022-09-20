
x = [int(x) for x in input().split()]

x.sort()

a = x[0]
b = x[1]
count = 0
if a == 1 and b == 1:
    print(0)
    exit()
while 1:
    a = a + 1
    b = b - 2
    #print(a , b)
    count = count + 1
    if a <= 0 or b <= 0:
        break
    c = min(a , b)
    d = max(a , b)
    a = c
    b = d
    
print(count)