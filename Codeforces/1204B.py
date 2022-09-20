
n , l , r = map(int , input().split())

mn = pow(2 , l) + (n - l) - 1
mx = pow(2 , r) + ((n - r) * pow(2 , r - 1)) - 1

print(mn , mx)