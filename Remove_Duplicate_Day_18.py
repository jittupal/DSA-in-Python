def remove_dup(arr):
    # Get the total number of elements in the array
    n = len(arr)

    # Create an empty dictionary (hash map) to store unique elements
    freq_map = {}

    # Step 1: Iterate through the array and add each element to freq_map
    # Using a dictionary automatically removes duplicates because keys are unique
    for i in range(0, n):
        freq_map[arr[i]] = 0   # value doesn't matter, we're just using keys

    # Step 2: Copy unique keys back to the array
    j = 0
    for k in freq_map:
        arr[j] = k   # overwrite original array with unique elements
        j += 1

    # Step 3: Print total count of unique elements
    print(f"Total Unique Element : {j}")

# Example array with duplicate elements
arr = [1, 1, 1, 2, 3, 3, 5, 7, 7, 8]

# Function call to remove duplicates
remove_dup(arr)
