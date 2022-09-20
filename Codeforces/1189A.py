
a = input()
b = input()
zero = b.count('0')
one = b.count('1')

if zero != one:
    print(1)
    print(b)
else:
    print(2)
    print(b[0] , b[1:])