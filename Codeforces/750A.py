

n , k = input().split()

n = int(n)

k = 240 - int(k)

for i in range(1, n + 1):
    a = i * 5
    if k >= a:
        k = k - a
        
    else:
        print(i - 1)
        exit()
print(n)
    