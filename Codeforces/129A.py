

n = int(input())
x = [int(x) for x in input().split()]

cnt = 0

for i in x:
    if (sum(x) - i) % 2 == 0:
        cnt += 1
        
print(cnt)