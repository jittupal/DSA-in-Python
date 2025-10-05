def selection(arr):
    # Get the length of the array
    n = len(arr)
    
    # Outer loop to move the boundary of the unsorted subarray
    for i in range(0, n):
        # Assume the current index has the smallest element
        mid = i
        
        # Inner loop to find the minimum element in the remaining unsorted array
        for j in range(i + 1, n):
            # If a smaller element is found, update the index of the minimum element
            if arr[mid] > arr[j]:
                mid = j
        
        # Swap the found minimum element with the first element of the unsorted part
        arr[mid], arr[i] = arr[i], arr[mid]


# Example array
arr = [2, 5, 9, 1, 3, 0, -1]

# Call the selection sort function
selection(arr)

# Print the sorted array
print(*arr)
