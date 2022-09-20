
n = int(input())

x = [int(x) for x in input().split()]

a = set(x)
l = list(a)
l.sort()
print('NO' if len(l) == 1 else l[1])
