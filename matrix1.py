def userinput(rows, cols):
    arr = [[0 for i in range(rows)] for j in range(cols)]

    for i in range(rows):
        for j in range(cols):
            arr[i][j] = int(input("Enter no. "))
    print()

    return arr

def multiply(arr1, arr2):
    if len(arr1[0]) != len(arr2):
        return "Matrix multiplication is not possible"
    
    result = [[0 for i in range(len(arr1))] for j in range(len(arr2))]
    
    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            for k in range(len(arr2)):
                result[i][j] += arr1[i][k]*arr2[k][j]
    
    return result

def addition(arr1, arr2):
    result = [[0 for i in range(len(arr1))] for j in range(len(arr2))]
    
    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
                result[i][j] += arr1[i][j] + arr2[i][j]

    return result

def subtraction(arr1, arr2):
    result = [[0 for i in range(len(arr1))] for j in range(len(arr2))]
    
    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
                result[i][j] += arr1[i][j] - arr2[i][j]

    return result

def transpose(arr):
    rows = len(arr)
    cols = len(arr[0])

    result = [[0 for i in range(rows)] for j in range(cols)]

    for i in range(rows):
        for j in range(cols):
            result[j][i] = arr[i][j]

    return result

def determinant(m):
    return (m[0][0]*minor(m, 0, 0)) - (m[0][1]*minor(m, 0, 1)) + (m[0][2]*minor(m, 0, 2))

def minor(m, row, col):
    temp = []
    for i in range(3):
        if i == row:
            continue
        for j in range(3):
            if j == col:
                continue
            temp.append(m[i][j])
    
    return ((temp[0]*temp[3]) - (temp[1]*temp[2]))
        
def cofactor(m):
    result = [[0 for i in range(3)]for j in range(3)]
    for i in range(3):
        for j in range(3):
            result[i][j] = ((-1)**(i+j)) * minor(m, i , j)
    
    return result

def inverse(m):
    det = determinant(m)
    if  det == 0:
        print("Inverse does not exist")
        return
    adj = transpose(cofactor(m))
    print("Inverse: ")
    for i in range(3):
        for j in range(3):
            adj[i][j] = adj[i][j]/det
            print(adj[i][j], end=" ")
        print()

r1 = int(input("Enter Rows for Matrix1: "))
c1= int(input("Enter Columns for Matrix1: "))
arr1 = userinput(r1, c1)

r2 = int(input("Enter Rows for Matrix2: "))
c2= int(input("Enter Columns for Matrix2: "))
arr2 = userinput(r2, c2)

print(arr1)
print(arr2)
print(f"Product of two matrices: {multiply(arr1, arr2)}")
print(f"Addition of two matrices: {addition(arr1, arr2)}")
print(f"Subtraction of two matrices: {subtraction(arr1, arr2)}")
print(f"Transposed Matrix is : {transpose(arr1)}")
inverse(arr1)