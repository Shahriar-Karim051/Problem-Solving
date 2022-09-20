s = 0
j = -1

for i in range(1, 41, 2):
    j = j + 1
    s = s + (i / pow(2 , j))
    
    
print('%.2f'%s)