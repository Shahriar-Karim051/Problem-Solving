

l = []
for i in range(20):
    a = int(input())
    l.append(a)
    
l.reverse()
for i in range(20):
    print('N[' + str(i) + '] =' , l[i])