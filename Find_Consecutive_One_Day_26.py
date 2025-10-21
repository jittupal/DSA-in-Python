def find_maxOne(arr):
    # Initialize a counter to track current consecutive 1s
    count = 0
    # Variable to store the maximum number of consecutive 1s found so far
    max_count = 0
    # Store the length of the array for iteration
    n = len(arr)

    # Loop through each element of the array
    for i in range(0, n):
        # If current element is 1, increase the current count
        if arr[i] == 1:
            count = count + 1
        else:
            # If we encounter a 0, it means the streak of 1s ended
            # Update max_count if current streak (count) is greater
            max_count = max(max_count, count)
            # Reset current count since the streak broke
            count = 0

    # After the loop ends, we again check max() in case
    # the array ends with a sequence of 1s (no 0 to trigger update)
    print(f"Max Consecutive One is : {max(max_count, count)}")


# Example array to test
arr = [0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1]
find_maxOne(arr)
