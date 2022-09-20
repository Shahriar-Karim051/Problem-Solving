

a = ['q' , 'w' ,'e' ,'r' ,'t' ,'y' ,'u' ,'i' ,'o' ,'p']

b = ['a' ,'s' ,'d' ,'f' ,'g' ,'h' ,'j' ,'k' ,'l' ,';']

c = ['z' ,'x' ,'c' ,'v' ,'b' ,'n' ,'m' ,',', '.' , '/']
y = input()
x = input()
x = list(x)

r = ''
if y == 'R':
    for i in range(len(x)):
        e = x[i]
        #print(e)
        if x[i] in a:
            r += a[a.index(e) - 1]
        elif x[i] in b:
            r += b[b.index(e) - 1]
        else:
            r += c[c.index(e) - 1]
else:
    for i in range(len(x)):
        e = x[i]
        if x[i] in a:
            r += a[a.index(e) + 1]
        elif x[i] in b:
            r += b[b.index(e) + 1]
        else:
            r += c[c.index(e) + 1]
            
print(r)