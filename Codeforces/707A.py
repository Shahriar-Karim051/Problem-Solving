
a , b = input().split()
a = int(a)

list = []

for i in range(a):
    x = input().split()
    #print(x)
    if "C" in x or "M" in x or "Y" in x:
        list.append(0)
        

if len(list) > 0:
    print("#Color")
else:
    print("#Black&White")