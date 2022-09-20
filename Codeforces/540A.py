
n = int(input())

a = input()

b = input()

count = 0

for i in range(len(a)):
    count = count + min(abs(int(a[i]) - int(b[i])) , (10 - abs(int(b[i]) - int(a[i]))))
    #print(count)
    
print(count)