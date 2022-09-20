
x = input()
a = b = 0
for i in x:
    if i == i.upper():
        a += 1
    else:
        b += 1
        
if a > b:
    print(x.upper())
else:
    print(x.lower())