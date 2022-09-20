

for i in range(int(input())):
    x = input()
    l = len(x)
    s = 0
    p = 0
    n = 4 * (int(x[0]) - 1) + l
    #print(n)
    s = (n // 4) * 10 + ((n % 4) * ((n % 4) + 1)) // 2
    print(s)