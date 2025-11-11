def find_first_occurrence(arr, k):
    """
    Binary search variant that returns the index of the first occurrence of k
    in a sorted list `arr`. If k is not present, prints -1.
    """
    n = len(arr)
    l = 0              # left boundary (inclusive)
    h = n - 1          # right boundary (inclusive)
    ans = -1           # store candidate index for first occurrence

    # Standard binary search loop with a tweak:
    # when arr[mid] == k we keep searching the left half to find earlier index.
    while l <= h:
        mid = (l + h) // 2

        if arr[mid] == k:
            ans = mid       # found k, record index
            h = mid - 1     # narrow search to left subarray to find first occurrence
        elif arr[mid] < k:
            l = mid + 1     # k must be in right half
        else:
            h = mid - 1     # k must be in left half

    print(f"first occurance {ans}")             # print final answer (or -1 if not found)


def find_last_occurrence(arr, k):
    """
    Binary search variant that returns the index of the last occurrence of k
    in a sorted list `arr`. If k is not present, prints -1.
    """
    n = len(arr)
    l = 0              # left boundary (inclusive)
    h = n - 1          # right boundary (inclusive)
    ans = -1           # store candidate index for last occurrence

    # Similar to first-occurrence search but when arr[mid] == k we move left boundary
    # to the right to continue searching for a later index.
    while l <= h:
        mid = (l + h) // 2

        if arr[mid] == k:
            ans = mid       # found k, record index
            l = mid + 1     # narrow search to right subarray to find last occurrence
        elif arr[mid] < k:
            l = mid + 1     # k must be in right half
        else:
            h = mid - 1     # k must be in left half

    print(f"last occurance {ans}")             # print final answer (or -1 if not found)


# Example usage:
# Sorted input required for binary search to work correctly.
arr = [1, 2, 3, 3, 3, 4, 4, 5, 5]
k = 3

find_first_occurrence(arr, k)   # expected output: index of first 3 -> 2
find_last_occurrence(arr, k)    # expected output: index of last 3  -> 4
