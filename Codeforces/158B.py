

n = int(input())

x = [int(x) for x in input().split()]

four = x.count(4)

three = x.count(3)

two = x.count(2)

one = x.count(1)


g = 0
if three > one:
    g = g + one
    three = three - one
    one = 0
else:
    g = g + three
    one = one - three
    three = 0
    
g = g + two // 2
two = two % 2

if one != 0 and two != 0:
    if one == 1:
        g = g + 1
        two = 0
        one = 0
    else:
        g = g + 1
        
        two = 0
        one = one - 2
    
g = g + one // 4
one = one % 4

if one != 0:
    g = g + 1
    one = 0
    
print(g + one + two + three + four)




