

for i in range(int(input())):
    x , y , z = map(int , input().split())
    if (x > y and x > z) or (y > x and y > z) or (z > x and z > y):
        print('NO')
    else:
        print('YES')
        print(min(x , y , z) , min(x , y , z) , max(x , y , z))
        