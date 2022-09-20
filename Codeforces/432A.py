

n , k = input().split()

k = int(k)

x = [int(x) for x in input().split()]
list = []
for i in x:
    if i + k <= 5:
        list.append(i)
        
print(len(list) // 3)