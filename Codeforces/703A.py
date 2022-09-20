
n = int(input())
mishka = chris = 0
for i in range(n):
    a , b = input().split()
    a = int(a)
    b = int(b)
    if a > b:
        mishka = mishka + 1
    elif b > a:
        chris = chris + 1
        
if mishka > chris:
    print("Mishka")
elif mishka < chris:
    print("Chris")
else:
    print("Friendship is magic!^^")