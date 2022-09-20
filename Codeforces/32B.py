import re

a = input()

a = re.sub('--' , '2' , a)
a = re.sub('-.' , '1' , a)


for i in a:
    if i == '.':
        print('0' , end = '')
    else:
        print(str(i) , end = '')
