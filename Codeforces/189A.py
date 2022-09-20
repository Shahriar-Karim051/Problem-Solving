
x , a , b , c = input().split()

x = int(x)
a = int(a)
b = int(b)
c = int(c)



list = []

list.append(a)
list.append(b)
list.append(c)

list.sort()

if a == 1 or b == 1 or c == 1:
    print(x)
    exit()
elif x == a and x == b and x == c:
    print(1)
    exit()

count = 1


for i in range(x):
    x = x - list[0]
    count = count + 1
    if x <= list[0] or x != list[1] or x != list[2]:
        break
    
print(count)