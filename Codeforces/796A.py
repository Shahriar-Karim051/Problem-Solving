

n , m , k = map(int , input().split())
m = m - 1
mn = n
x = [int(x) for x in input().split()]

for i in range(len(x)):
    if i != m and x[i] != 0 and k >= x[i]:
        mn = min(mn , abs(m - i))
        
print(mn * 10)