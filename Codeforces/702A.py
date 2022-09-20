
a = input()

x = [int(x) for x in input().split()]

count = 1
best = 0

for i in range(len(x) - 1):
    if x[i] < x[i + 1]:
        count = count + 1
        #print(count)
    else:
        if best < count:
            best = count
            count = 1
        else:
            count = 1
        
print(max(best , count))