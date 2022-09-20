

a , b , c = map(int , input().split())

print((a + c) * 2 if a == b else (min(a , b) + c) * 2 + 1)