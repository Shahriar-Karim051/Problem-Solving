




a = int(input())

list = []

for i in range (a):
    b = input()
    if len(b) > 10:
        c = b[0] + str(len(b) - 2) + b[len(b) - 1]
        list.append(c)
    else:
        list.append(b)
        
        
for d in list:
    print(str(d))