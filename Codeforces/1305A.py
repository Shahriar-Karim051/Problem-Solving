
for i in range(int(input())):
    n = input()
    a = [int(a) for a in input().split()]
    a.sort()
    b = [int(b) for b in input().split()]
    b.sort()
    for j in a:
        print(str(j) , end = ' ')
    print()
    for j in b:
        print(str(j) , end = ' ')