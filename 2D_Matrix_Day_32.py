# example 2D list (matrix)
arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# print diagonal and upper-triangle elements; print '*' for lower-triangle
rows = len(arr)        # number of rows in matrix
cols = len(arr[0])     # number of columns in matrix (assumes at least one row)

for i in range(0, rows):          # iterate over each row index
    for j in range(0, cols):      # iterate over each column index
        if j >= i:
            # when column index >= row index, we are on or above main diagonal
            print(arr[i][j], end="  ")
        else:
            # below main diagonal — print placeholder
            print("*", end="  ")
    print()   # new line after each row

# prepare an empty matrix to hold the transpose
# transpose will have 'cols' rows and 'rows' columns
transpos_list = [[0] * rows for _ in range(cols)]

# fill the transpose: element at (i, j) in original becomes (j, i) in transpose
for i in range(0, rows):
    for j in range(0, cols):
        transpos_list[j][i] = arr[i][j]

# print the transposed matrix
# for a square matrix rows == cols; if not square, you may want to iterate:
# for i in range(cols):
#     for j in range(rows):
#         ...
for i in range(0, rows):
    for j in range(0, cols):
        print(transpos_list[i][j], end="  ")
    print()