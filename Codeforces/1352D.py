

for i in range(int(input())):
    n = int(input())
    a = [int(a) for a in input().split()]
    prev = moves = 0
    total = [0 , 0]
    while len(a) != 0:
        moves += 1
        cur = 0
        while len(a) != 0 and cur <= prev:
            cur += a[0]
            a.remove(a[0])
        total[moves % 2] += cur
        prev = cur
        a.reverse()
    print(moves , total[1] , total[0])
        