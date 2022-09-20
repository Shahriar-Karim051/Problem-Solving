count = 0
l = []
for i in range(6):
    a = float(input())
    if a > 0:
        count = count + 1
        l.append(a)
        
print(count , 'valores positivos')

avg = sum(l) / len(l)

print('%.1f'%avg)