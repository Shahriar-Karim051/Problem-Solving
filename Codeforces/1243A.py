
for i in range(int(input())):
    a = input()
    x = [int(x) for x in input().split()]
    x.sort(reverse = True)
    cnt = 0
    for j in range(len(x)):
        if x[j] >= j + 1:
            cnt += 1
    print(cnt)