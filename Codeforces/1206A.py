
a = input()

b = [int(b) for b in input().split()]
b.sort()
c = input()

d = [int(d) for d in input().split()]
d.sort()
print(b[-1] , d[-1])