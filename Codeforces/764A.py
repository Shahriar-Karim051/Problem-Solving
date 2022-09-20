import math

n , m , z = map(int , input().split())


a = math.gcd(n , m)

b = n * m // a


        
print(z // b)
    