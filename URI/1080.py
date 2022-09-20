mx = 0
pos = 0

for i in range(1,101):
    a = int(input())
    if a > mx:
        mx = a
        pos = i
        
print(mx)
print(pos)