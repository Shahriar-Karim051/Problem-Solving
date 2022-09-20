
x = input()


count = 0

for i in x:
    if i == '4' or i == '7':
        count += 1
        
        
count = str(count)
#print(count)
for j in count:
    if j != '4' and j != '7':
        print("NO")
        exit()
    
print("YES")  