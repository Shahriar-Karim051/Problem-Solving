

a = input()

l1 = [int(l1) for l1 in input().split()]

l2 = []



l2.extend(l1)

l1.sort()



for i in range(int(input())):
    x = [int(x) for x in input().split()]
    if x[0] == 1:
        print(sum(l2[x[1] - 1 : x[2]]))
    else:
        print(sum(l1[x[1] - 1 : x[2]]))
