
a , b = input().split()
a = int(a)
b = int(b)
first = second = draw = 0
for i in range(1 , 7):
    if abs(a - i) < abs(b - i):
        first = first + 1
    elif abs(a - i) > abs(b - i):
        second = second + 1
    else:
        draw = draw + 1
        
print(first , draw , second)
    