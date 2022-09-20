

l = ['purple', 'green', 'blue', 'orange', 'red', 'yellow']
m = []
cnt = 0
for i in range(int(input())):
    a = input()
    if a in l:
        l.remove(a)
        
    
print(len(l))
for j in l:
    if j == 'purple': 
        print('Power')
    elif j == 'green':
        print('Time')
    elif j == 'blue':
        print('Space')
    elif j == 'orange':
        print('Soul')
    elif j == 'red':
        print('Reality')
            
    else:
        print('Mind')
            



