
a = float(input())

if a <= 400:
    b = a * 0.15
    c = a + b
    print("Novo salario:" , '%.2f'%c)
    print("Reajuste ganho:" , '%.2f'%b)
    print("Em percentual: 15 %")
elif a >= 400.01 and a <= 800.00:
    b = a * 0.12
    c = a + b
    print("Novo salario:" , '%.2f'%c)
    print("Reajuste ganho:" , '%.2f'%b)
    print("Em percentual: 12 %")
elif a >= 800.01 and a <= 1200:
    b = a * 0.10
    c = a + b
    print("Novo salario:" , '%.2f'%c)
    print("Reajuste ganho:" , '%.2f'%b)
    print("Em percentual: 10 %")
elif a >= 1200.01 and a <= 2000:
    b = a * 0.07
    c = a + b
    print("Novo salario:" , '%.2f'%c)
    print("Reajuste ganho:" , '%.2f'%b)
    print("Em percentual: 7 %")
elif a > 2000.00:
    b = a * 0.04
    c = a + b
    print("Novo salario:" , '%.2f'%c)
    print("Reajuste ganho:" , '%.2f'%b)
    print("Em percentual: 4 %")