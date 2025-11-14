def findposition(arr, target):
    #Count  the total length of array
    n = len(arr)
    #start the lowest index from 0
    l = 0
    #start the highest index from the end of the array
    h = n -1
    #run until low and high overlap
    while l <= h:
        #find the search area where element can be happen
        mid = ( l + h ) // 2
        #we find our element at index mid
        if arr[mid] == target:
            print(f"The index of Target is:  {mid}")
            break
        #if found element is greater than target then we must search in the left from mid index where elements are less than target
        elif arr[mid] > target:
            h = mid - 1
        #if found element is less than target then we must search in the right area of array because all the element are greater than target there.
        else:
            l = mid + 1
        
    print(f"The insert position will be: {l}")

arr = [1, 2, 3, 4, 4, 4, 5, 7, 8, 8]

findposition(arr, 9)