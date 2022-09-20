
s = input()
l = [0] * len(s)
for j in range(1 , len(s)):
        if s[j] == s[j - 1]:
            l[j] = l[j - 1] + 1
        else:
            l[j] = l[j - 1]

ls = []
rs = []
m = int(input())
for i in range(m):
    a , r = map(int , input().split())
    #print(l[r - 1] - l[a - 1])
    ls.append(a)
    rs.append(r)
    
for i in range(m):
    print(l[rs[i] - 1] - l[ls[i] - 1])
    

