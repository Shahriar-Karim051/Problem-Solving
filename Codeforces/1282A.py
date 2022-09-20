

for i in range(int(input())):
    a , b , c , r = map(int , input().split())
    cnt = 0
    beg = max(c - r , min(a , b))
    end = min(c + r , max(a , b))
    print(abs(a - b) - max(0 , end - beg))
    