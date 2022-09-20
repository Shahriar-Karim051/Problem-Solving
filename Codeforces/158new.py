
a1 ,b1 = input().split()

b = int(b1)
a = int(a1)

x = [int(x) for x in input().split()] 

p = x[b - 1]
count = 0
for i in range(len(x)):
    if int(x[i]) >= p and x[i] != 0:
        #print(int(x[i]))
        count = count + 1
        
        
print(count)