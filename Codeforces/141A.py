
a = input()
b = input()
c = input()

d = a + b

if len(d) != len(c):
    print("NO")
    exit()
else:
    for i in d:
        if d.count(i) != c.count(i):
            print("NO")
            exit()


        
print("YES")