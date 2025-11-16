def find_minimum(arr):
    #start from the starting index
    l = 0
    #start from last index of array
    h = len(arr) - 1
    #initialize the variable with positive infinite value
    mini = float("inf")
    #run until end index is lower than start index
    while l <= h:
        #find the mid to find the search space
        mid = (l + h) // 2
        #if value of mid element and last element in increasing manner
        #then it can be possible that mid element is smallest
        if arr[mid] <= arr[h]:
            mini = min(mini, arr[mid])
            #smallest element will be on left side of mid
            h = mid - 1
        #if value of mid element is greater then last element then it is not in increassing manner
        #then it is possible that mid element is smallest
        else:
            mini = min(mini, arr[mid])
            #smallest elment will be on right side of mid if mid element > last element
            l = mid + 1
    
    print("Mininum element in Array is:: ", mini)

arr = [8, 9, 1, 4, 5, 6]
find_minimum(arr)