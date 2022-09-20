

def ss(a , b):
    m = len(a)
    n = len(b)
    i = 0
    j = 0
    while i < m and j < n:
        if a[i] == b[j]:
            i += 1
        j += 1
    return i == m


a = 'heidi'
b = input()

print('YES' if ss(a , b) else 'NO')