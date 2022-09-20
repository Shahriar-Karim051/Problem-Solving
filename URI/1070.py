
a = int(input())

if a % 2 == 0:
    a = a - 1
else:
    a = a - 2
for i in range(6):
    a = a + 2
    print(a)