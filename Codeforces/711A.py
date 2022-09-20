l = []

import re
r = 0
for i in range(int(input())):
    x = input()
    if r != 1:
        if 'OO' in x:
            x = re.sub("OO" , "++" , x , 1)
            l.append(x)
            r = 1
        else:
            l.append(x)
    else:
        l.append(x)
        
        
if r == 1:
    print('YES')
    for j in range(len(l)):
        print(str(l[j]))
else:
    print('NO')
        
            