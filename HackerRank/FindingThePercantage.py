dic = {}
for i in range(int(input())):
    a , b , c , d = input().split()
    dic[a] = (float(b) + float(c) + float(d)) / 3
    
e = dic[input()]

print('%.2f'%e)
    