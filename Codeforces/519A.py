
w = b = 0
for i in range(8):
    x = input()
    for i in range(len(x)):
        
        if x[i] == 'Q':
            w = w + 9
        elif x[i] == 'q':
            b = b + 9
        elif x[i] == 'R':
            w = w + 5
        elif x[i] == 'r':
            b = b + 5
        elif x[i] == 'B':
            w = w + 3
        elif x[i] == 'b':
            b = b + 3
        elif x[i] == 'N':
            w = w + 3
        elif x[i] == 'n':
            b = b + 3
        elif x[i] == 'P':
            w = w + 1
        elif x[i] == 'p':
            b = b + 1
            
if b > w:
    print('Black')
elif w > b:
    print('White')
else:
    print('Draw')
            