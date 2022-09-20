
n = int(input())
a = 0

for i in range(n + 2):
    a = ((i * (i + 1)) // 2) + a
    
    if a > n:
        print(i - 1)
        break