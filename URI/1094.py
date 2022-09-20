
n = int(input())
total = c = r = s = 0
for i in range(n):
    a , b = input().split()
    a = int(a)
    total = total + a
    if b == 'C':
        c = c + a
    elif b == 'R':
        r = r + a
    elif b == 'S':
        s = s + a
        
pc = (c / total) * 100
pr = (r / total) * 100
ps = (s / total) * 100

print("Total:" , total , "cobaias")
print("Total de coelhos:" , c)
print("Total de ratos:" , r)
print("Total de sapos:" , s)
print("Percentual de coelhos:" , '%.2f'%pc , '%')
print("Percentual de ratos:" , '%.2f'%pr , '%')
print("Percentual de sapos:" , '%.2f'%ps , '%')

    
    