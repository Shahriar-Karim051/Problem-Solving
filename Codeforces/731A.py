

n = input()
s = 0
a = 'a'

for i in range(len(n)):
    s = s + min(abs(ord(n[i]) - ord(a)) , 26 - abs(ord(n[i]) - ord(a)))
    a = n[i]
    
print(s)

