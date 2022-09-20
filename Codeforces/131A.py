
x = input()
y = len(x) - 1
if x[0] == x[0].lower():
    for i in range(y):
        z = i+1
        if x[z] != x[z].upper():
            print(x)
            exit()
    print(x[0].upper() + x[1 : ].lower() )
else:
    for j in range(y):
        b = j + 1
        if x[b] != x[b].upper():
            print(x)
            exit()
    print(x.lower())
    
            
            

