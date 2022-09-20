
n = input()
a = input()

l = []

for i in a:
    if i == '2':
        l.append(2)
    elif i == '3':
        l.append(3)
    elif i == '4':
        l.append(3)
        l.append(2)
        l.append(2)
    elif i == '5':
        l.append(5)
    elif i == '6':
        l.append(3)
        l.append(5)
    elif i == '7':
        l.append(7)
    elif i == '8':
        l.append(2)
        l.append(2)
        l.append(2)
        l.append(7)
    elif i == '9':
        l.append(2)
        l.append(3)
        l.append(3)
        l.append(7)
        
l.sort(reverse = True)

for j in l:
    print(j , end = '')