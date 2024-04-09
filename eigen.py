import math

def eigenvector(vector, value):
    for i in range(len(vector)):
        for j in range(len(vector[0])):
            if i == j:
                vector[i][j] -= value
    return vector

def findRoots(a, b, c):
    d = (b*b) - (4*a*c)
    s1 = (-b - math.sqrt(d)) / (a + a)
    s2 = (-b + math.sqrt(d)) / (a + a)
    return [-s1, -s2]

def eigenvalue(vector):
    a = 1
    b = vector[0][0] + vector[1][1]
    c = vector[0][0] * vector[1][1] - vector[0][1] * vector[1][0]

    roots = findRoots(a, b, c)
    print(f"Roots: {roots}")

    for root in roots:
        print(f"Eigenvector for {root}: {eigenvector(vector, root)}")

# Take user input for matrix elements
m = []
print("Enter the elements of the 2x2 matrix:")
for i in range(2):
    row = []
    for j in range(2):
        element = float(input(f"Enter element [{i+1},{j+1}]: "))
        row.append(element)
    m.append(row)

eigenvalue(m)
