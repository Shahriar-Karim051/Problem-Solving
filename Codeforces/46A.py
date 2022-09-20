

n = int(input())
s = 1

for i in range(1 , n):
    s += i
    if s > n:
        s = s % n
    print(s , end = ' ')