

n , a , b = map(int , input().split())

print(((a - 1 + b) % n + n) % n + 1)