
n , h , m = map(int , input().split())
p = [h for i in range(n)]
for i in range(m):
    l , r , x = map(int , input().split())
    for j in range(l-1 , r):
        p[j] = min(p[j] , x)
        
print(sum(map(lambda n: n * n , p)))