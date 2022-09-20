n = int(input())

a = (n // 2) + 1
count = 0
for i in range(1,a):
    if n % i == 0:
        count = count + 1
        
print(count)