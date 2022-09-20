
a , b = map(int , input().split())
s = 0
for i in range(a):
    c , d = map(int , input().split())
    if c <= b:
        s = s + d
        
print(s)