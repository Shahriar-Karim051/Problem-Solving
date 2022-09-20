

import re
a = input()

z = re.compile(r'BA')
d = z.search(str(a))
if d == None:
    print('NO')
else:
    p = re.compile(r'AB')
    e = p.search(str(a))
    if e == None:
        print('NO')
    else:
        x = re.compile(r'AB.*BA')
        b = x.search(str(a))
        y = re.compile(r'BA.*AB')
        c = y.search(str(a))
        if c != None or b != None :
            print('YES')
        else:
            print('NO')
    


