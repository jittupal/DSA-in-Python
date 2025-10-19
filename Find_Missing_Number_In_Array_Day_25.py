# ------------------------------------------
# 🧠 Dictionary Approach (Hash Map Method)
# ------------------------------------------

def find_missing(arr):
    n = len(arr)  # Length of the given array
    freq_map = {}  # Create an empty dictionary to track numbers

    # Step 1: Initialize all keys from 0 to n with value 0
    # This assumes the array should contain numbers from 0 to n
    for i in range(0, n + 1):   # ✅ Corrected: should go till n, not n-1
        freq_map[i] = 0

    # Step 2: Mark numbers that are present in the array
    for num in arr:
        freq_map[num] = 1  # Mark as found

    # Step 3: Find which number is missing (value still 0)
    for k, v in freq_map.items():
        if v == 0:
            return k  # Return the missing number


# Example 1
arr = [1, 4, 6, 8, 3, 5, 7, 0]
ans = find_missing(arr)
print(f"Missing number from array is : {ans}")
# Output: Missing number from array is : 2


# ------------------------------------------
# ⚡ Very Optimized Approach (Mathematical Formula)
# ------------------------------------------

# Example 2
arr = [1, 3, 5, 7, 4, 6, 0]
n = len(arr)  # Length of array

# Step 1: Formula for sum of first n natural numbers = n*(n+1)/2
# Step 2: Subtract the actual sum of the array from the expected sum
# The difference gives the missing number
expected_sum = n * (n + 1) // 2   # ✅ Use '*' instead of function call
actual_sum = sum(arr)
ans = expected_sum - actual_sum

print(f"The missing number is : {ans}")
# Output: The missing number is : 2
