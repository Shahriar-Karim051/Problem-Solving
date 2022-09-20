
n = int(input())
x = [int(x) for x in input().split()]

l = []
for i in range(n):
    l.append([x[i] , i + 1])
    
l.sort(reverse = True)

shot = 0
j = 0
for i in l:
    shot += i[0] * j + 1
    j += 1
        
print(shot)

for i in l:
    print(i[1] , end = ' ')
    
