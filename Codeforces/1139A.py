
a = int(input())

x = input()
s = 0
for i in range(a):
    if int(x[i]) != 0 and int(x[i]) % 2 == 0:
        s = s + i + 1

print(s)