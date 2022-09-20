
s , n = input().split()

s = int(s)
n = int(n)

list = []
for i in range(n):
    x = [x for x in map(int, input().split())]
    list.append(x)
    



for a , b in sorted(list):
    if s > a:
        s = s + b
    else:
        print("NO")
        exit()





print("YES")