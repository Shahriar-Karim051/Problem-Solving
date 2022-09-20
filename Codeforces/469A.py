import re
n = int(input())

a = input()
a = re.sub(a[0], "a" , a , 1)
b = input()
b = re.sub(b[0], "b" , b , 1)

for i in range(1 , n + 1):
    if str(i) not in a and str(i) not in b:
        print("Oh, my keyboard!")
        exit()

print("I become the guy.")
    