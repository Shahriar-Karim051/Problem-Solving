
a , b = input().split()
a = int(a)
b = int(b)

for i in range(1 , a + 1):
    if i % 2 != 0:
        print('#' * b)
    elif i % 4 != 0:
        print('.' * (b - 1) + '#')
    else:
        print('#' + '.' * (b - 1))