

x = input()

a = ['h','e','l','l','o']

i = -1

for c in a:
    i = x.find(c,i+1)
    if i == -1:
        print("NO")
        exit()
        
print("YES")