
a = input()

a = a.lower()


s = ""

for i in range(len(a)):
    if a[i] != 'a' and a[i] != 'e' and a[i] != 'i' and a[i] != 'o' and a[i] != 'u' and a[i] != 'y':
        #print(a[i])
        s += '.'
        s += a[i]


print(s)