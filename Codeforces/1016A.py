

n , m = map(int , input().split())

a = [int(a) for a in input().split()]

rem = 0

for i in a:
    print((i + rem) // m , end = ' ')
    rem = (i + rem) % m
    
