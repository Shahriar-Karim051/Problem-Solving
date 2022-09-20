
a = input()



x = [int(x) for x in input().split()]
s = 0
for i in x:
    i = i + s
    s = max(s , i)
    print(i , end = ' ')
    