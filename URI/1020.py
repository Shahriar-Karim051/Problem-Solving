
a = int(input())

b = a // 365
print(b , 'ano(s)')
a = a % 365

c = a // 30
print(c , 'mes(es)')
a = a % 30

print(a , 'dia(s)')