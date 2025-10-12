def remove_duplicate(arr):
    n = len(arr)
    if n == 1:
        print(f"Total Number of Unique Element is : {1}")
    i = 0
    j = i+1
    while j<n:
        if arr[i] != arr[j]:
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
        j = j+1
    
    print(f"Total Number of Unique Element is : {i+1}")


arr = [1,1 ,1, 3, 3, 6, 6, 9, 9, 11]
remove_duplicate(arr)