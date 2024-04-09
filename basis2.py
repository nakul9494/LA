def determinant(m):
    det = (m[0][0] * m[1][1]) - (m[0][1] * m[1][0])
    return det

def cofactor(m):
    matrix = [[0 for i in range(2)] for j in range(2)]
    matrix[0][0] = m[1][1]
    matrix[0][1] = -m[0][1]
    matrix[1][0] = -m[1][0]
    matrix[1][1] = m[0][0]
    return matrix

def inverse(m):
    det = determinant(m)
    if det == 0:
        print("inverse doesn't exist")
        return
    adj = cofactor(m)
    for i in range(2):
        for j in range(2):
            adj[i][j] = adj[i][j]/det
    return adj

def transpose(m):
    try:
        copy = [[0 for j in range(len(m))] for i in range(len(m[0]))]
    except TypeError:
        return [[n] for n in m]
    
    for i in range(len(m)):
        for j in range(len(m[0])):
            copy[i][j] = m[j][i]
    
    return copy

def multiply(arr1,arr2):
    return [[sum(a*b for a,b in zip(arow,bcol)) for bcol in zip(*arr2)] for arow in arr1]


def changeBasis(oldbasis,newbasis,vector):
    adj1 = transpose(oldbasis)
    adj2 = transpose(newbasis)
    inv1 = inverse(adj1)
    inv2 = inverse(adj2)
    result = multiply(multiply(inv1,inv2),transpose(vector))
    return result

# Take user input for the matrices and vector
m1 = []
print("Enter the elements of the standard basis matrix (2x2):")
for i in range(2):
    row = []
    for j in range(2):
        element = float(input(f"Enter element [{i+1},{j+1}]: "))
        row.append(element)
    m1.append(row)

s = []
print("Enter the elements of the basis matrix S (2x2):")
for i in range(2):
    row = []
    for j in range(2):
        element = float(input(f"Enter element [{i+1},{j+1}]: "))
        row.append(element)
    s.append(row)

vector = []
print("Enter the elements of the vector (2 elements):")
for i in range(2):
    element = float(input(f"Enter element [{i+1}]: "))
    vector.append(element)

# Find coordinates with respect to basis S
print("Result:", changeBasis(m1, s, vector))
