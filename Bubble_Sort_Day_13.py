def bubble(arr):
    # Outer loop runs from 'n' down to 0 (controls number of passes)
    for i in range(n, -1, -1):
        is_swaped = False  # Flag to check if any swap occurred in this pass
        
        # Inner loop runs from 0 to i (compares adjacent elements)
        for j in range(0, i + 1):
            # Compare current element with the next one
            if arr[j] > arr[j + 1]:
                # If current element is greater, swap them
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                is_swaped = True  # Mark that a swap has happened
        
        # If no swap happened in this pass, array is already sorted
        if is_swaped == False:
            break  # Exit early (optimization to stop unnecessary passes)


# Initial unsorted array
arr = [2, 5, 3, 4, 7, 1, 6]

# Find the length of array
n = len(arr)

# Since inside bubble() we access arr[j+1], reduce n by 2 to prevent index out of range
n = n - 2

# Call the bubble sort function
bubble(arr)

# Print the sorted array
print(*arr)
