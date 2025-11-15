def floor_ceil(arr, x):
    #if floor or cieling is not in the array then return -1
    floor = -1
    ciel = -1
    #start from very first index
    l = 0
    #start from very end index
    h = len(arr) - 1
    #run the loop until low and high is overlap to each other
    while l <= h:
        #find the search space by comparing the mid value
        mid = (l + h) // 2
        #if x is found in the array then the cieling and floor is the same number
        if arr[mid] == x:
            floor = arr[mid]
            ciel = arr[mid]
            break
        #if mid element is greater than x then it might be cieling so we store the element
        elif arr[mid] > x:
            ciel = arr[mid]
            #we can assume that, there will more element which is less than mid element
            #but can be greater than x so we can search on left area from mid
            h = mid - 1
            #if the mid element is less than x then it might be floor so we can store it in answer
        else:
            floor = arr[mid]
            #we can assume that, there will more element which is greater than mid element
            #but can be less than x so we can search on right area of mid
            l = mid + 1
    
    print(f"Floor of {x} is: {floor} and Ciel of {x} is: {ciel}")

#array can contain duplicate elements also
arr = [1, 1, 1, 3, 3, 5, 5, 5, 5, 7,7, 7, 7, 8, 9]

floor_ceil(arr, 6)
