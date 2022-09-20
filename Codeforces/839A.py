
n , k = map(int , input().split())
a = [int(a) for a in input().split()]

arya = bran = day = 0

for i in a:
    arya += i
    if arya <= 8:
        bran += arya
        arya = 0
        day += 1
    else:
        bran += 8
        arya -= 8
        day += 1
        
    if bran >= k:
        print(day)
        exit()
    
print(-1)