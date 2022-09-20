

a = int(input())

mx = 2 + (a * 2)

for i in range(1 , (a // 2) + 2):
    if a % i == 0:
        per = 2 * i + 2 * (a // i)
        mx = min(mx , per)
        
print(mx)