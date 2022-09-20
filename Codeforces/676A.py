

n = int(input())

x = [int(x) for x in input().split()]

a = x.index(max(x))
b = x.index(min(x))

print(max(a , b , n - 1 - a , n - 1 - b))