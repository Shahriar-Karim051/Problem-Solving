
coin = 0
coin1 = 0
n = int(input())
x = [int(x) for x in input().split()]
x.sort()
mid = n // 2
mid1 = n // 2 + 1

for i in range(n):
    if abs(x[i] - mid) % 2 != 0:
        coin += 1
    if abs(x[i] - mid1) % 2 != 0:
        coin1 += 1
print(min(coin , coin1))
        
    

