
for i in range(int(input())):
    l = []
    for j in range(9):
        x = input()
        x = list(x)
        for k in range(len(x)):
            if x[k] == '9':
                x[k] = '8'
        l.append((x))
    for m in l:
        print(''.join(m))
            