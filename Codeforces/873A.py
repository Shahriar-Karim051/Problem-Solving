
n , k , x = map(int , input().split())

y = [int(y) for y in input().split()]

print(sum(y[:len(y) - k]) + k * x)