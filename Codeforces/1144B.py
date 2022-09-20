

n = int(input())
x = [int(x) for x in input().split()]
x.sort()

even = []
odd = []

for i in x:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
        
if abs(len(even) - len(odd)) <= 1:
    print(0)
elif len(even) > len(odd):
    print(sum(even[ : len(even) - len(odd) - 1]))
else:
    print(sum(odd[ : len(odd) - len(even) - 1]))