
a = int(input())

x = [int(x) for x in input().split()]
count = 1
z = len(x) - 1
l = []
y = ""
for i in range(z):
    j = i + 1
    if x[i] <= x[j]:
        count +=1
        #print(count)
    else:
        l.append(count)
        count = 1
l.append(count)   
        #print(count)
  
if len(l) == 1:
    for i in l:
        print(str(i))
        
    
else:
    l.sort(reverse = True)
    for i in l:
        print(str(i))
        break
    
    
    
    
    