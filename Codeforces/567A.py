
n = int(input())
x = [int(x) for x in input().split()]

print(abs(x[0] - x[1]) , x[-1] - x[0])

for i in range(1 , n - 1):
    print(min(x[i] - x[i - 1] , x[i + 1] - x[i]) , max(x[i] - x[0], x[-1] - x[i]) )
    
print(x[-1] - x[-2] , x[-1] - x[0])