z = int(input())
x = input()

a = b = 0

for i in x:
    if i == 'A':
        a = a + 1
    else:
        b = b + 1
        
        
if a > b:
    print("Anton")
elif b > a:
    print("Danik")
else:
    print("Friendship")
    