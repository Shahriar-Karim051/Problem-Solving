
n = int(input())
a = [int(a) for a in input().split()]

num = [0] * 100050
mx = 0

for i in a:
    num[i] = num[i] + 1
    mx = max(mx , i)    
f = [0] * 100050

f[1] = num[1]


for j in range(2 , mx + 1):
    f[j] = max(f[j - 1], f[j - 2] + j * num[j])
    
print(f[mx])
    