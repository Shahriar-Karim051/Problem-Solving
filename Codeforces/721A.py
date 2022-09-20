
n = int(input())

x = input()
l = []
c = 0
if x[0] == 'B':
    c = c + 1
    for i in range(1 , len(x)):
        if x[i] == 'B':
            c = c + 1
        else:
            if x[i - 1] == 'B':
                l.append(c)
                c = 0
            else:
                c = 0
    if x[-1] == 'B':
        l.append(c)
    
                
else:
    c = 0
    for i in range(1 , len(x)):
        if x[i] == 'B':
            c = c + 1
        else:
            if x[i - 1] == 'B':
                l.append(c)
                c = 0
            else:
                c = 0
    if x[-1] == 'B':
        l.append(c)
    
            
        
print(len(l))


for i in l:
    print(str(i) , end = ' ')