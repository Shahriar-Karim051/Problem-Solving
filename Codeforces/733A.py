
n = input()
a = 0

mx = 0

for i in range(len(n)):
    if n[i] == 'A' or n[i] == 'E' or n[i] == 'I' or n[i] == 'O' or n[i] == 'U' or n[i] == 'Y':
        a = a + 1
        mx = max(mx , a)
        a = 0
    else:
        a = a + 1
        
mx = max(mx , a + 1)
        
print(mx)
    