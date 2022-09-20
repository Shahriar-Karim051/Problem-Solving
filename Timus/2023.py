

a = ['A' , 'P' , 'O' , 'R']
b = ['B' , 'M' , 'S']
c = ['D' , 'G' , 'J' , 'K' , 'T' , 'W']

pos = 1
s = 0

for i in range(int(input())):
    n = input()
    if n[0] in a:
        p = 1
    elif n[0] in b:
        p = 2
    elif n[0] in c:
        p = 3
    s = s + abs(pos - p)
    pos = p
    
print(s)