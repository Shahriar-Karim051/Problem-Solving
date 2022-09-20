

n = int(input())
x = [int(x) for x in input().split()]

a = x.index(max(x))

x.sort()

print(a + 1 , x[-2])