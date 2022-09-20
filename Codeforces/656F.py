
a = input()
s = 1
for i in range(1 , len(a)):
    if a[i] == '0':
        s = s + 9
    else:
        s = s + int(a[i])
        
print(s)
        