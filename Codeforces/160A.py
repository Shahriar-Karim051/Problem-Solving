
z = int(input())

x = [int(x) for x in input().split()]
x.sort(reverse = True)
#print(x)
s = sum(x)

a = 0
count = 0
#print(s)

for i in x:
    a = a + i
    count += 1
    s = s -i
    if a > s:
        print(count)
        break
    
    