
for i in range(int(input())):
    n , m = map(int , input().split())
    a = [int(a) for a in input().split()]
    print('YES' if sum(a) == m else 'NO')
    
    