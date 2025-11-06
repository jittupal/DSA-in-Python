def setZero(arr, row, col):
    # Helper that marks (using a sentinel) all cells in given row and column
    # except existing zeros. We don't set zeros immediately to avoid cascading
    # effects (new zeros causing further rows/cols to be zeroed).
    # arr: matrix, row/col: indices of a zero found earlier.
    r = len(arr)
    c = len(arr[0])

    # mark entire column 'col' in every row with sentinel if not already zero
    for i in range(0, r):
        if arr[i][col] != 0:
            arr[i][col] = float("inf")  # sentinel value

    # mark entire row 'row' in every column with sentinel if not already zero
    for j in range(0, c):
        if arr[row][j] != 0:
            arr[row][j] = float("inf")  # sentinel value


def matrixZero(arr):
    # Main algorithm using sentinel marking:
    # 1) First pass: whenever we encounter a 0, call setZero to mark its row
    #    and column with a sentinel (float("inf")) so we don't immediately
    #    modify other cells that might later be discovered as zeros.
    # 2) Second pass: convert all sentinels to 0.
    # 3) Print the resulting matrix.
    rows = len(arr)
    cols = len(arr[0])

    # mark positions to be zeroed using sentinel
    for i in range(rows):
        for j in range(cols):
            if arr[i][j] == 0:
                setZero(arr, i, j)

    # replace sentinels with actual zeros
    for i in range(rows):
        for j in range(cols):
            if arr[i][j] == float("inf"):
                arr[i][j] = 0

    # print matrix row by row
    for i in range(rows):
        for j in range(cols):
            print(arr[i][j], end="  ")
        print()


def setMatrixZeroes(mat):
    # Alternative approach that uses auxiliary trackers (rowtrack, coltrack).
    # Steps:
    # 1) Scan matrix and record which rows and columns must be zeroed.
    # 2) Second pass: set cells to 0 if their row or column is marked.
    #
    # This approach avoids using sentinels and performs two clear passes.
    r = len(mat)
    c = len(mat[0])

    # trackers initialized to 0; we'll mark as -1 when that row/col must be zeroed
    rowtrack = [0 for _ in range(r)]
    coltrack = [0 for _ in range(c)]

    # first pass: record rows/cols that contain a zero
    for i in range(0, r):
        for j in range(0, c):
            if mat[i][j] == 0:
                rowtrack[i] = -1
                coltrack[j] = -1

    # second pass: if a cell's row or column is marked, set it to zero
    for i in range(0, r):
        for j in range(0, c):
            if rowtrack[i] == -1 or coltrack[j] == -1:
                mat[i][j] = 0

    # print the final matrix (use 'mat' which is the local variable here)
    for i in range(r):
        for j in range(c):
            print(mat[i][j], end="  ")
        print()


# example matrix used for testing the two functions
arr = [[0, 2, 3, 8], [1, 2, 3, 4], [7, 8, 9, 0]]

# run the sentinel-based implementation and print result
matrixZero(arr)

# reset example matrix (so second function runs on the original input)
arr = [[0, 2, 3, 8], [1, 2, 3, 4], [7, 8, 9, 0]]

# run the tracker-based implementation and print result
setMatrixZeroes(arr)