def rotate(arr):
    n = len(arr)
    # If length is 1 then we can return arr
    if n == 1:
        return arr
    # if length is 2 then we can just swap 1st and 2nd element
    if n == 2:
        arr[0], arr[1] = arr[1], arr[0]
        return arr
    #by using slicing we can get the last element and we can add the last element with the rest of the remaining element
    arr[:] = [arr[-1]] + arr[:n-1]
    return arr


arr = [ 1, 2, 6, 9, 0, 3]
arr = rotate(arr)
print(*arr)