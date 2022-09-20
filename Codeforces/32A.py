

n , d = map(int , input().split())

x = [int(x) for x in input().split()]
cnt = 0
for i in x:
    for j in x:
        if abs(i - j) <= d:
            cnt += 1
            
print(cnt - n)