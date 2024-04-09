def gaussianElimination(m):
    rows = len(m)
    cols = len(m[0])
    for i in range(rows):
        if m[i][i] == 0.0:
            return "invalid"
        for j in range(rows):
            if i != j:
                factor = m[j][i] / m[i][i]
                for k in range(cols):
                    m[j][k] = m[j][k] - factor * m[i][k]

    for i in range(rows):
        factor = m[i][i]
        for j in range(cols):
            m[i][j] = round(m[i][j] / factor)
    return [row[-1] for row in m]

# Get matrix dimensions from user
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

# Initialize the matrix with zeros
m = [[0.0 for a in range(cols)] for b in range(rows)]

# Get matrix elements from user
for i in range(rows):
    for j in range(cols):
        m[i][j] = float(input(f"Enter element at row {i+1}, column {j+1}: "))

print(f"this is gaussian elimination: {gaussianElimination(m)}")

