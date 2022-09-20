

n = int(input())
t = [int(t) for t in input().split()]
a = tuple(t)
print(hash(a))