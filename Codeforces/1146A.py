
n = input()

c = n.count('a')


if c == len(n):
    print(c)
elif 2 * c - 1 > len(n):
    print(len(n))
else:
    print(2 * c - 1)