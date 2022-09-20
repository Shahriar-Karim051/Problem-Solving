

for i in range(int(input())):
    x , y = map(int , input().split())
    a , b = map(int , input().split())
    c = min(x , y)
    d = max(x , y) - c
    s1 = (d * a) + (c * b)
    s2 = a * (x + y)
    e = max(x , y)
    s3 = (b * c) + (a * d)
    print(min(s1 , s2, s3))