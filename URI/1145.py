
a , b = input().split()

a = int(a)
b = int(b)

for i in range(1 , b + 1):
    print(i , end = ' ')
    if i % a == 0:
        print()