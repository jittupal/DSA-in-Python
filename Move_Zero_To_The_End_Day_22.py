def movement(arr):
    n = len(arr)
    #if the length of list/array is 1 then no need to do anything
    if n == 1:
        return
    i = 0
    #find the first 0 from left, if find then stop loop at that 0
    while i < n:
        if arr[i] == 0:
            break
        i += 1
    
    #if there is no 0 in array then do nothing simple return
    if i == n:
        return
    #find next non zero element just after finding the first 0
    j = i + 1
    while j < n:
        #if find then swap and then keep moving
        if arr[j] != 0:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
        j += 1
    

arr = [1, 0, 2, 0, 3, 0, 4, 0, 5, 0]
movement(arr)
#print the whole array
print(*arr)