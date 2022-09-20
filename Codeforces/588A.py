meat = []
price = []
for i in range(int(input())):
    a , b = map(int , input().split())
    meat.append(a)
    price.append(b)

meat.append(0)
price.append(0)
    

value = 0
for j in range(len(meat) - 1):
    value += meat[j] * price[j]
    if price[j] < price[j + 1]:
        price[j + 1] = price[j]
        
print(value)
    
    