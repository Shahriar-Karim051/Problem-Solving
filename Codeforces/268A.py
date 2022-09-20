home = []
away = []
cnt = 0
for i in range(int(input())):
    a , b = input().split()
    home.append(a)
    away.append(b)
    
for j in range(len(home)):
    for k in range(len(away)):
        if home[j] == away[k] and j != k :
            cnt = cnt + 1
            
                
print(cnt)