
a , b = input().split()

a = int(a)
b = int(b)

if a == b:
    print("O JOGO DUROU 24 HORA(S)")
elif a > b:
    c = (24 - a) + b
    print("O JOGO DUROU" , c , "HORA(S)" )
elif a < b:
    c = b - a
    print("O JOGO DUROU" , c , "HORA(S)" )
    