
import math
for i in range(int(input())):
    n , k = map(int , input().split())
    ans = n
    if n <= k:
        print(1)
    else:
        for j in range(1 , int(math.sqrt(n)) + 1):
            if n % j == 0:
                if j <= k:
                    ans = min(ans , n // j)
                    
                if (n // j) <= k:
                    ans = min(ans , j)
        print(ans)