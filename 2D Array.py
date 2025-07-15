row = int(input("Enter number of rows required:\n"))
matrix = []
for i in range(row):
    rows = []
    column = int(input(f"Enter number of columns requied for row {i+1}:\n"))
    for j in range(column):
        elmnt = int(input("Enter elements required:\n"))
        rows.append(elmnt)
    matrix.append(rows)
print(matrix)
