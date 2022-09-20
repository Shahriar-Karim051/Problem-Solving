
x = [int(x) for x in input().split()]

drink = (x[1] * x[2]) // x[6]
lime = x[3] * x[4]
salt = x[5] // x[7]
    

print(min(drink, lime, salt) // x[0])