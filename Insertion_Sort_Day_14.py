# --------------------------
# Iterative Insertion Sort
# --------------------------
def insert(arr):
    n = len(arr)
    # Outer loop goes from 1 to n-1
    # Each iteration inserts arr[i] into the sorted portion arr[0...i-1]
    for i in range(1, n):
        j = i - 1        # j points to the last index of the sorted portion
        key = arr[i]     # Element to be inserted in the sorted portion

        # Shift elements greater than 'key' one position to the right
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j = j - 1    # Move one step left

        # Place the key at its correct position
        arr[j + 1] = key


# --------------------------
# Recursive helper function
# (acts like the inner while-loop)
# --------------------------
def loop_recur(arr, key, j):
    """
    This function shifts elements to the right recursively
    until the correct position for 'key' is found.
    It returns the index 'j' where the key should finally be inserted.
    """
    # Base condition:
    # If j is out of bounds (j < 0)
    # or arr[j] <= key (we found correct position)
    if j >= 0 and arr[j] > key:
        # Shift arr[j] to the right
        arr[j + 1] = arr[j]
        # Recursively check the previous element
    else:
        # Once the correct spot is found (arr[j] <= key or j < 0),
        # return the current index j
        return j

    # Recursive call: move left and continue comparing
    return loop_recur(arr, key, j - 1)


# --------------------------
# Recursive Insertion Sort
# --------------------------
def inser_recur(arr, i, n):
    """
    Recursive version of insertion sort.
    i represents the current index being inserted.
    """
    # Base condition: stop when we reach the end of the array
    if i >= n:
        return

    j = i - 1            # Compare current element with elements to its left
    key = arr[i]         # Element to insert into the sorted part

    # Call the recursive 'loop_recur' to shift elements
    a = loop_recur(arr, key, j)

    # Place 'key' at the correct position returned by loop_recur
    arr[a + 1] = key

    # Recursively call for the next element
    inser_recur(arr, i + 1, n)


# --------------------------
# Driver Code
# --------------------------
arr = [3, 5, 4, 6, 1, 2, 0, 7]

n = len(arr)
i = 1   # Start from index 1 since the first element is already "sorted"

# Perform recursive insertion sort
inser_recur(arr, i, n)
print("After recursive insertion sort:", *arr)

# Perform iterative insertion sort (for verification)
insert(arr)
print("After iterative insertion sort:", *arr)
