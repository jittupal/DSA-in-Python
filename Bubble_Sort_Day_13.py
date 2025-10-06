def bubble(arr):
    # Iterative Bubble Sort version
    
    # Outer loop runs from n down to 0 (controls number of passes)
    for i in range(n, -1, -1):
        is_swaped = False  # Flag to detect if any swaps occurred
        
        # Inner loop compares adjacent elements from 0 to i
        for j in range(0, i + 1):
            # Compare current element with the next one
            if arr[j] > arr[j + 1]:
                # If current element is greater, swap them
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                is_swaped = True  # Mark that a swap happened
        
        # Optimization: if no swap occurred, array is already sorted
        if is_swaped == False:
            break  # Exit early (saves unnecessary passes)


def recur_bubble(arr, i):
    # Recursive Bubble Sort version
    
    # Base condition: stop recursion when i < 0 (fully sorted)
    if i <= -1:
        return
    
    is_swaped = False  # Track if a swap happens in this pass
    
    # One full pass of bubble sort (largest element goes to end)
    for j in range(0, i + 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            is_swaped = True  # A swap happened this round
    
    # If no swap happened, array is sorted — stop recursion
    if is_swaped == False:
        return
    
    # Recursive call for the remaining unsorted part (i-1)
    recur_bubble(arr, i - 1)


# ---------------------------------------
# DRIVER CODE
# ---------------------------------------

# Initial unsorted array
arr = [2, 5, 3, 4, 7, 1, 6]

# Find the length of array
n = len(arr)

# Since inside bubble() we access arr[j+1], reduce n by 2 to prevent index out of range
n = n - 2

# First: run recursive bubble sort
recur_bubble(arr, n)

# Print sorted result after recursion
print("After Recursive Bubble Sort:", *arr)

# Now call the iterative version on already sorted array
bubble(arr)

# Print result after iterative version
print("After Iterative Bubble Sort:", *arr)
