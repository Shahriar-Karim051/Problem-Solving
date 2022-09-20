for i in range(int(input())):  
    a , b = map(int , input().split())

    cnt = 0

    while 1:
        if a == b:
            print(cnt)
            break
        elif a > b:
            if abs(a - b) == 1:
                b = b + 1
                cnt += 1
            elif abs(a - b) == 2:
                b = b + 2
                cnt += 1
            else:
                if abs(a - b) > 5:
                    cnt = cnt + abs(a - b) // 5
                    b = b + abs(a - b) - (abs(a - b) % 5)
                
                else:
                    b = b + 5
                    cnt += 1
                
        else:
            if abs(a - b) == 1:
                a = a + 1
                cnt += 1
            elif abs(a - b) == 2:
                a = a + 2
                cnt += 1
            else:
                if abs(a - b) > 5:
                    cnt = cnt + abs(a - b) // 5
                    a = a + abs(a - b) - (abs(a - b) % 5)
                    
                    
                    
                else:
                    a = a + 5
                    cnt += 1
                