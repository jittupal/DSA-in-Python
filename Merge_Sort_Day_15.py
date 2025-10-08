def merge_array(left, right):
    # Initialize pointers for both halves
    i, j = 0, 0
    # Get lengths of left and right subarrays
    n, m = len(left), len(right)
    # Temporary list to store merged result
    result = []

    # Merge elements while both halves still have unprocessed items
    while i < n and j < m:
        # Compare current elements of both halves
        if left[i] <= right[j]:
            # If element in 'left' is smaller, add it to result
            result.append(left[i])
            i = i + 1
        else:
            # Otherwise, take element from 'right'
            result.append(right[j])
            j = j + 1

    # If there are remaining elements in 'left' half, add them all
    while i < n:
        result.append(left[i])
        i = i + 1

    # If there are remaining elements in 'right' half, add them all
    while j < m:
        result.append(right[j])
        j = j + 1

    # Return the fully merged and sorted list
    return result


def mergesort(arr):
    # Base case: if array has 0 or 1 element, it’s already sorted
    if len(arr) <= 1:
        return arr

    # Find the midpoint to divide the array
    mid = len(arr) // 2

    # Divide the array into two halves
    left_arr = arr[:mid]
    right_arr = arr[mid:]

    # Recursively sort both halves
    left = mergesort(left_arr)
    right = mergesort(right_arr)

    # Merge the two sorted halves into a single sorted list
    return merge_array(left, right)


# Example usage
arr = [7, 4, 6, 3, 0, 1, 5, 2]

# Call mergesort to get a sorted version of arr
sorted_array = mergesort(arr)

# Print the sorted elements separated by space
print(*sorted_array)
