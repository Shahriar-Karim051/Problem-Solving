from collections import Counter

for i in range(int(input())):
    a = int(input())
    x = [int(x) for x in input().split()]
    diff = len(set(x))
    s = Counter(x)
    c , same = s.most_common(1)[0]
    print(max(min(same - 1, diff), min(same, diff - 1)))