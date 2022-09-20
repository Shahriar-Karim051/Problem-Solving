

for i in range(int(input())):
    l , r = map(int , input().split())
    print('YES' if r - l < l else 'NO')