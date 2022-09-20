
from collections import Counter


n = input()

x = [int(x) for x in input().split()]

c = Counter(x)



if len(c) == len(x):
    print(1)
else:
    for i in c.most_common(1):
        print(i[1])