def setZero(arr, row, col):
    r = len(arr)
    c = len(arr[0])

    # set entire column 'col' to sentinel (iterate rows)
    for i in range(0, r):
        if arr[i][col] != 0:
            arr[i][col] = float("inf")

    # set entire row 'row' to sentinel (iterate columns)
    for j in range(0, c):
        if arr[row][j] != 0:
            arr[row][j] = float("inf")

def matrixZero(arr):
    rows = len(arr)
    cols = len(arr[0])

    # mark positions to be zeroed using sentinel
    for i in range(rows):
        for j in range(cols):
            if arr[i][j] == 0:
                setZero(arr, i, j)

    # replace sentinels with 0
    for i in range(rows):
        for j in range(cols):
            if arr[i][j] == float("inf"):
                arr[i][j] = 0

    # print matrix row by row
    for i in range(rows):
        for j in range(cols):
            print(arr[i][j], end="  ")
        print()

arr = [[0, 2, 3, 8], [1, 2, 3, 4], [7, 8, 9, 0]]

matrixZero(arr)