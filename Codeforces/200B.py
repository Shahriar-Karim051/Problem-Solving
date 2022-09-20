
a = int(input())

x = [int(x) for x in input().split()]
sum = 0
for i in x:
    sum = sum + i

print(sum / a)