def echelon(m):
    rows = len(m)
    cols = len(m[0])
    for i in range(rows):
        if m[i][i] == 0.0:
            return "Invalid"
        for j in range(rows):
            if i != j:
                factor = m[j][i] / m[i][i]
                for k in range(cols):
                    m[j][k] = m[j][k] - factor * m[i][k]        
    result = []
    for row in m:
        if any(row):
            result.append(row)
    return result

def rowCanonical(m):
    m = echelon(m)
    rows = len(m)
    cols = len(m[0])
    for i in range(rows):
        factor = m[i][i]
        for j in range(cols):
            m[i][j] = round(m[i][j] / factor)
    [print(row) for row in m]

# Take user input for matrix dimensions and elements
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

m = []
print("Enter the elements of the matrix row-wise:")
for i in range(rows):
    row = []
    for j in range(cols):
        element = float(input(f"Enter element [{i+1},{j+1}]: "))
        row.append(element)
    m.append(row)

rowCanonical(m)

print(echelon(m))
