def two_sum(arr, target):
    n = len(arr)  # Get the length of the array
    hash_map = {}  # Initialize an empty dictionary to store visited numbers and their indices

    # Loop through each element in the array
    for i in range(0, n):
        remaining = target - arr[i]  # Calculate the number needed to reach the target sum
        
        # Check if that "remaining" number already exists in the hash_map
        if remaining in hash_map:
            # If found, we print both indices that form the target sum
            print(f"The two numbers are at indices: {[hash_map[remaining], i]} (values: {arr[hash_map[remaining]]}, {arr[i]})")
        
        # Store the current number with its index in hash_map
        # This helps us quickly check for future elements
        hash_map[arr[i]] = i


# Example usage
arr = [1, 3, 5, 7, 9, 4]
target = 14
two_sum(arr, target)