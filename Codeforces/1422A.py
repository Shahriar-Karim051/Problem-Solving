

for i in range(int(input())):
    a , b , c = map(int , input().split())
    a , b , c = sorted((a , b , c))
    print(c + (b - a))