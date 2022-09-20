
a = int(input())
s = input()
n = 0


for j in s:
    if j == '+':
        n += 1
    else:
        n -= 1
        if n == - 1:
            n = 0
        

print(n)
    