# Function to reverse a portion (subarray) of the list 'arr'
def reverse(arr, left, right):
    # Keep swapping elements until the two pointers meet
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]  # swap elements
        left = left + 1    # move left pointer forward
        right = right - 1  # move right pointer backward


# Original array
arr = [1, 2, 3, 4, 5, 9]
# Number of positions to rotate the array (clockwise)
k = 3
# Length of the array
n = len(arr)

# Step 1: Reverse the last 'k' elements
# For k = 4, this reverses elements at indexes 2 to 5 → [3, 4, 5, 9] becomes [9, 5, 4, 3]
reverse(arr, n-k, n-1)

# Step 2: Reverse the first 'n-k' elements
# This reverses the first 2 elements → [1, 2] becomes [2, 1]
reverse(arr, 0, n-k-1)

# Step 3: Reverse the entire array
# Now, reversing the whole array gives the final rotated form
reverse(arr, 0, n-1)

# Print the rotated array
print(*arr)
