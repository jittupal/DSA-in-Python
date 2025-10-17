def searche(arr, x):
    n = len(arr)
    for i in range(0, n):
        if arr[i] == x:
            return 1
    return -1


arr = [1, 2, 3, 4, 5, 6, 8, 9]
x = 5
ans = searche(arr, 10)
if ans == 1:
    print("Element found")
else:
    print("Element Not Found")