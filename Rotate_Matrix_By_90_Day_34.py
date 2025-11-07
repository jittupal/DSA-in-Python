def rotate(mat):
    """
    Rotate square matrix `mat` 90 degrees clockwise in-place.
    Approach:
      1. Transpose the matrix (swap mat[i][j] with mat[j][i] for j>i).
      2. Reverse each row to complete the 90-degree clockwise rotation.
    Works in-place and uses O(1) extra space (besides input).
    """
    r = len(mat)            # number of rows
    c = len(mat[0])         # number of columns (assumes non-empty matrix)

    # If matrix is 1x1 nothing to do
    if r == 1 and c == 1:
        return

    # Transpose step:
    # For each pair (i, j) with j > i, swap mat[i][j] and mat[j][i].
    # This converts rows into columns (mirror across main diagonal).
    for i in range(0, r - 1):
        for j in range(i + 1, r):
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]

    # Reverse each row:
    # After transposition, reversing every row yields the matrix rotated
    # 90 degrees clockwise.
    for i in range(0, r):
        mat[i].reverse()


# example usage and printing
mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

rotate(mat)

# print the rotated matrix row by row
r = len(mat)
c = len(mat[0])
for i in range(0, r):
    for j in range(0, c):
        print(mat[i][j], end="  ")
    print()