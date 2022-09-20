

n = int(input())

one = []
two = []
three = []

x = [int(x) for x in input().split()]
cnt = 0
for i in range(n):
    if x[i] == 1:
        one.append(i + 1)
    elif x[i] == 2:
        two.append(i + 1)
    else:
        three.append(i + 1)
        
cnt = min(len(one), len(two), len(three))                       
print(cnt)     
                   
for j in range(cnt):
    print(one[j] , two[j] , three[j])
                        
    