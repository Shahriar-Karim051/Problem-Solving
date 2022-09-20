
n = input()

a = n.index('.')
b = int(n[:a])
c = int(n[a + 1])

if n[a - 1] == '9':
    print('GOTO Vasilisa.')
else:
    print(b if c <= 4 else b + 1)