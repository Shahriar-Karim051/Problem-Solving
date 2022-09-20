

w , h = map(int , input().split())
u1 , d1 = map(int , input().split())
u2 , d2 = map(int , input().split())

while h > 0:
    if h == d1:
        w = w + h
        w = w - u1
        h -= 1
    elif h == d2:
        w = w + h
        w = w - u2
        h -= 1
    else:
        w = w + h
        h -= 1
    if w < 0:
        w = 0
    
    
    
    
print(w)