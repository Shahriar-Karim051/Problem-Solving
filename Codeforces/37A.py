

from collections import Counter

a = int(input())

x = [int(x) for x in input().split()]

m , n = Counter(x).most_common(1)[0]


c = len(set(x))
print(n , c)