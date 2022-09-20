
x = input()
list = []

s = ''
p = ''
for i in range(len(x)):
    if x[i] != '+':
        list.append(x[i])
        
list.sort()
     

for j in list:
    #print(str(j))
    #if str(j) != "a":
    s += str(j)
    s += '+'
    
        
for k in range(len(s)-1):
    p += s[k]

print(p)