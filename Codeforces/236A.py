 
x = input()

l = []

for i in x:
    if i not in l:
        l.append(i)
        #print(i)
        #print(l)

if len(l) % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")

