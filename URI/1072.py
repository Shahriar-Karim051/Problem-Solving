
n = int(input())
o = 0
for i in range(n):
    a = int(input())
    if a >= 10 and a <= 20:
        o = o + 1
        
print(o , 'in')
print(n - o , 'out')