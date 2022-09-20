

a = input()

b = list(a)

for i in range(len(a)):
    if b[i] == '0':
        del b[i]
        break
if len(a) == len(b):
    del b[-1]
       
print(''.join(b))
    