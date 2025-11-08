def spiral_traver(arr):
    # Initialize boundaries for the current rectangle to traverse:
    # top and left start at 0, bottom and right start at last indices.
    top = 0
    left = 0
    bottom = len(arr) - 1
    right = len(arr[0]) - 1

    # ans collects the spiral order; itera is a debug counter printed in code
    ans = []
    itera = 1

    # Guard: if matrix is empty or has empty rows, return empty result
    if not arr or not arr[0]:
        return []

    # Continue while there is a valid sub-rectangle to traverse
    while top <= bottom and left <= right:
        # 1) Traverse the top row from left to right
        #    Columns go from 'left' to 'right' at row index 'top'.
        for i in range(left, right+1):
            ans.append(arr[top][i])
            print(itera)          # debug: shows progression
        top += 1                  # top row consumed, move boundary down
        itera += 1

        # 2) Traverse the right column from top to bottom
        #    Rows go from current 'top' to 'bottom' at column 'right'.
        for i in range(top, bottom+1):
            ans.append(arr[i][right])
            print(itera)          # debug
        right -= 1                # right column consumed, move boundary left
        itera += 1

        # 3) Traverse the bottom row from right to left (if that row still exists)
        #    Check left <= right to avoid duplicate traversal when single column remains.
        if left <= right:
            for i in range(right, left-1, -1):
                print("first if condition")  # debug marker
                ans.append(arr[bottom][i])
                print(itera)
        bottom -= 1               # bottom row consumed, move boundary up
        itera += 1

        # 4) Traverse the left column from bottom to top (if that column still exists)
        #    Check top <= bottom to avoid duplicate traversal when single row remains.
        if top <= bottom:
            for i in range(bottom, top-1, -1):
                print("Second If condition")  # debug marker
                ans.append(arr[i][left])
                print(itera)
        left += 1                 # left column consumed, move boundary right
        itera += 1

    # At this point ans holds the spiral order; function currently does not return it,
    # but prints debug values during traversal. You can return ans if you want to use it.
    # return ans

# example usage: builds a 3x3 matrix and runs the traversal (debug prints will appear)
arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
spiral_traver(arr)