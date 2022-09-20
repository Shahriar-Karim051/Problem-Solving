

x = input()
y = input()
j = 0
cnt = 1
for i in range(len(y)):
    if x[j] == y[i]:
        j = j + 1
        cnt = cnt + 1
        
print(cnt)
    