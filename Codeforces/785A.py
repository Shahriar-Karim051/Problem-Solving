
a = int(input())
count = 0
for i in range(a):
    b = input()
    if b == "Tetrahedron":
        count = count + 4
    elif b == "Cube":
        count = count + 6
    elif b == "Octahedron":
        count = count + 8
    elif b == "Dodecahedron":
        count = count + 12
    else:
        count = count + 20
    
    
print(count)