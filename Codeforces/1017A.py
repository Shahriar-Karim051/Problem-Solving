

n = int(input())

x = [int(x) for x in input().split()]

mx  = sum(x)
count = 1

for i in range(n - 1):
    x = [int(x) for x in input().split()]
    if sum(x) > mx:
        count = count + 1
        
print(count)