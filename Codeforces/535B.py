

n = input()
ans = 1
for x in n:
    if x == '7':
        ans = 2 * ans + 1
    else:
        ans = 2 * ans
print(ans - 1)
