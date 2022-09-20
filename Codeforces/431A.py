

a , b , c , d = map(int , input().split())

x = input()
s = 0
for i in x:
    if i == '1':
        s = s + a
    elif i == '2':
        s = s + b
    elif i == '3':
        s = s + c
    else:
        s = s + d
        
print(s)
    
        