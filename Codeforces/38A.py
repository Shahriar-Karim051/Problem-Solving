
s = 0
n = int(input())
d = [int(d) for d in input().split()]
a , b = map(int , input().split())
for j in range(a , b):
    s = s + d[j - 1]
print(s)