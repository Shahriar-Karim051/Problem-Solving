

for i in range(int(input())):
    x = [int(x) for x in input().split()]
    x[0] -= 1
    x[1] -= 1
    x[2] -= 1
    mx = sum(x) * 10000
    for j in range(3):
        for k in range(3):
            for l in range(3):
                a = x[0] + j
                b = x[1] + k
                c = x[2] + l
                mx = min(mx , (abs(a - b) + abs(a - c) + abs(b - c)))
                
    print(mx)