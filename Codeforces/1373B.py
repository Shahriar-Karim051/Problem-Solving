

for i in range(int(input())):
    a = input()
    zero = a.count('0')
    one = a.count('1')
    if min(zero , one) % 2 == 1:
        print('DA')
    else:
        print('NET')