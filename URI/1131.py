
count = aw = bw = draw = 0

while 1:
    a , b = input().split()
    a = int(a)
    b = int(b)
    count = count + 1
    if a > b:
        aw = aw + 1
    elif a < b:
        bw = bw + 1
    elif a == b:
        draw = draw + 1
    print('Novo grenal (1-sim 2-nao)')
    c = input()
    if c == '2':
        break
print(count , 'grenais')
print('Inter:' + str(aw))
print('Gremio:' + str(bw))
print('Empates:' + str(draw))

if aw > bw:
    print('Inter venceu mais')
elif aw < bw:
    print('Gremio venceu mais')
else:
    print('Não houve vencedor')
    