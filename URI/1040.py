
x = [float(x) for x in input().split()]

avg = ((x[0] * 2) + (x[1] * 3) + (x[2] * 4) + x[3]) / (2 + 3 + 4 + 1)

print("Media:" , '%.1f'%avg)

if avg >= 7.0:
    print("Aluno aprovado." )
elif avg < 5.0:
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    a = float(input())
    print("Nota do exame:" , a)
    a = (avg + a) / 2
    if a >= 5.0:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print("Media final:" , '%.1f'%a)