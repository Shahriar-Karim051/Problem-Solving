
n = int(input())

for i in range(n):
    a = input()
    b = [int(b) for b in input().split()]
    if sum(b) % 2 != 0:
        print("YES")
    else:
        count1 = sum(map(lambda x : x % 2 == 1 , b))
        count2 = sum(map(lambda y : y % 2 == 0 , b))
        if count1 > 0 and count2 > 0:
            print("YES")
        else:
            print("NO")
    