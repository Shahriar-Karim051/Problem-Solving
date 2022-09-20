
a = input()
x = [int(x) for x in input().split()]
s = 0
l = []
b = input()
y = [int(y) for y in input().split()]
for i in x:
    s = s + i
    l.append(s)
ind = 0 
w = []  
for j in range(1 , s + 1):
    if j > l[ind]:
        ind += 1
    w.append(ind + 1)    
for k in y:
    print(w[k - 1])
    
