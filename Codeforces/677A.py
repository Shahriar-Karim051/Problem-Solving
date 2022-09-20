x , h = input().split()

h = int(h)

a = [int(a) for a in input().split()]
count = 0
for i in a:
    if i > h:
        count = count + 2
    else:
        count = count + 1
        
print(count)