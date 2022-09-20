a = int(input())

n = input()
n = list(n)
cnt = 0

for i in range(0 , a , 2):
    if n[i] == n[i + 1]:
        cnt = cnt + 1
        if n[i] == 'a':
            n[i] = 'b'
        else:
            n[i] = 'a'
        
            
        
            
print(cnt)
print(''.join(n))
            