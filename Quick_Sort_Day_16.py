def partition(arr, low, high):
    # Choose the first element as the pivot
    pivot = arr[low]
    # Initialize two pointers: i (from left), j (from right)
    i, j = low, high

    # Loop until the two pointers cross
    while i < j:

        # Move 'i' right until you find an element greater than pivot
        # or reach the end of the array segment
        while arr[i] <= pivot and i <= high - 1:
            i += 1

        # Move 'j' left until you find an element smaller than or equal to pivot
        # or reach the beginning of the segment
        while arr[j] > pivot and j >= low + 1:
            j -= 1

        # If i < j, swap elements at i and j to correct their positions
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    # Finally, swap pivot element (arr[low]) with element at j
    # So pivot gets placed at its correct sorted position
    arr[j], arr[low] = arr[low], arr[j]

    # Return the pivot index (where it is now correctly placed)
    return j


def quick_sort(arr, low, high):
    # Base condition: only sort if low < high
    if low < high:
        # Partition the array and get the pivot index
        p_ind = partition(arr, low, high)

        # Recursively sort the left half (elements < pivot)
        quick_sort(arr, low, p_ind - 1)

        # Recursively sort the right half (elements > pivot)
        quick_sort(arr, p_ind + 1, high)


# --- Main program ---
arr = [4, 3, 6, 5, 2, 1, 7]
n = len(arr)

# Call quick sort on full array
quick_sort(arr, 0, n - 1)

# Print the sorted array
print(*arr)
