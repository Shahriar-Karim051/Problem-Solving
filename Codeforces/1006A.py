
a = input()

x = [int(x) for x in input().split()]
r = ''
for i in x:
    if i % 2 == 0:
        i = i - 1
        r += str(i) + ' '
        
    else:
        r += str(i) + ' '
        
print(r)