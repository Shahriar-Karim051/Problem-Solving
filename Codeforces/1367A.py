
for i in range(int(input())):
    n = input()
    n = list(n)
    a = ''
    a += n[0]
    a += n[1]
    for j in range(len(n)):
        if j > 2 and j % 2 == 1:
            a += n[j]
    print(a)