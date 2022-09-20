
x = int(input())
count = 0
while x > 0:
    if x % 2 != 0:
        count = count + 1
    x = x // 2

print(count)