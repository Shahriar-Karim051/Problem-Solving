t = int(input())
for i in range(t):
    n , x = map(int , input().split())
    a = [int(a) for a in input().split()]
    a.sort()
    b = [int(b) for b in input().split()]
    b.sort(reverse = True)
    if i < t - 1:
        m = input()
    c = 0
    if n == 1:
        print('Yes' if a[0] + b[0] <= x else 'No')
    else:
        for j in range(n):
            if a[j] + b[j] > x:
                c = 1
                break
        print('Yes' if c == 0 else 'No')
    
    