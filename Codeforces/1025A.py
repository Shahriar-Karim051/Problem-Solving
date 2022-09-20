from collections import Counter

n = int(input())


if n == 1:
    print('YES')
    exit()
x = input()
x = list(x)

a , b = Counter(x).most_common(1)[0]

print('YES' if b > 1 else 'NO')