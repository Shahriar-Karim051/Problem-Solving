import re
n = input()
x = re.findall('\d' , n)
y = re.findall('[a-z]' , n)
z = re.findall('[A-Z]' , n)
if len(n) >= 5 and x and y and z:
    print('Correct')
else:
    print('Too weak')