
n = input()

x = [int(x) for x in input().split()]

even = []

odd = []

for i in range(len(x)):
    if x[i] % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
#print(even)
#print(odd)
if len(even) == 1:
    print(even[0] + 1)
else:
    print(odd[0] + 1)