
n = int(input())

a = [int(a) for a in input().split()]


b = [int(b) for b in input().split()]
b.sort()

print('YES' if sum(a) <= b[-1] + b[-2] else 'NO')