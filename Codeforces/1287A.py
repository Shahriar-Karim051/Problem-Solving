
n = int(input())


for i in range(n):
    a = int(input())
    b = input()
    cnt = 0
    l = []
    b += 'C'
    for j in range(len(b)):
        if b[j] == 'A':
            for k in range(j + 1 , len(b)):
                if b[k] == 'P':
                    cnt = cnt + 1
                else:
                    l.append(cnt)
                    cnt = 0
                    break
        elif b[j] == 'C':
            l.append(cnt)
    l.sort()
    print(l[-1])
        
     
                    
            
            