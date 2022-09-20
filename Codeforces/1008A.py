

vow = ['a' , 'e' , 'i' , 'o' , 'u']

s = input()

if s[-1] != 'n' and s[-1] not in vow:
    print('NO')
    exit()
else:
    for i in range(len(s) - 1):
        if s[i] != 'n' and s[i] not in vow:
            if s[i + 1] not in vow:
                print('NO')
                exit()
print('YES')