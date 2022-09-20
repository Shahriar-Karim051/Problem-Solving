
n = int(input())

x = [int(x) for x in input().split()]

mn = x[0]
d = 1
r = 0

for i in range(1 , n):
    if x[i] < mn:
        mn = x[i]
        d = i + 1
        r = 0
    elif x[i] == mn:
        r = 1
        
print(d if r == 0 else 'Still Rozdil')