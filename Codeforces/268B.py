
n = int(input())

s = n

for i in range(1,n):
    s = s + (n - i) * i
    
print(s)