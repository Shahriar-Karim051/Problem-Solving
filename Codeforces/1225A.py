
a , b = map(int , input().split())

if a == b:
    print(str(a) + str(1) , str(b) + str(2))
elif a == 9 and b == 1:
    print(9 , 10)
elif a + 1 == b:
    print(str(a) + str(9) , str(b) + str(0))
else:
    print(-1)