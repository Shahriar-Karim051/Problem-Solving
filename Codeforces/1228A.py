
a , b = input().split()

a = int(a)
b = int(b) + 1

for i in range(a , b):
    if len(set(str(i))) == len(str(i)):
        print(i)
        exit()
    
print(-1)