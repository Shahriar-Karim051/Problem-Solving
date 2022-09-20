

n = int(input())

l = ["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"]

a = 1

while 5 * a < n:
    n = n - (5 * a)
    a = a * 2
 
print(l[(n - 1) // a])