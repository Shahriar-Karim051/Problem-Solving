

n , a , b = map(int , input().split())

x = [int(x) for x in input().split()]
x.sort()

print(x[b] - x[b - 1])