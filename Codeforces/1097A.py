


a = input()
cnt = 0
x = [str(x) for x in input().split()]
for i in x:
    if a[0] in i[0] or a[1] in i[1]:
       cnt = 1
       break
   
if cnt == 1:
    print('YES')
else:
    print('NO')