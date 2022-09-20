
n , m = map(int , input().split())
a = [0] * m
b = [0] * m
c = [0] * m
d = [0] * m
e = [0] * m
for i in range(n):
    s = input()
    for j in range(len(s)):
        if s[j] == 'A':
            a[j] += 1
        elif s[j] == 'B':
            b[j] += 1
        elif s[j] == 'C':
            c[j] += 1
        elif s[j] == 'D':
            d[j] += 1
        else:
            e[j] += 1
        
        
    
mk = [int(mk) for mk in input().split()]
marks = 0
for i in range(m):
    marks += max(a[i] , b[i] , c[i] , d[i] , e[i]) * mk[i]
    
print(marks)