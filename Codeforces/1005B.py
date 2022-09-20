

s = input()
t = input()
cnt = 0
for i in range(1 , min(len(s) , len(t)) + 1):
    if s[-i] == t[-i]:
        cnt += 1
    else:
        break
    
print(len(s) + len(t) - (2 * cnt))