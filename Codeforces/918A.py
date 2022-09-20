
n = int(input())
l = [1]

a = b = 1
r = ''
while b < n:
    c = a + b
    l.append(c)
    a = b
    b = c
    
for i in range(1 , n + 1):
    if i in l:
        r += 'O'
    else:
        r += 'o'

print(r)