
a = int(input())

b = a // 3600
a = a % 3600

c = a // 60
a = a % 60

print(str(b) + ':' + str(c) + ':' + str(a))