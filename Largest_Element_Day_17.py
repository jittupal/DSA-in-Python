def large_element(arr):
    # Initialize 'largest' with the first element of the array
    largest = arr[0]
    
    # Get the length of the array
    n = len(arr)
    
    # Traverse the array from index 0 to n-1
    for i in range(0, n):
        # Compare current element with 'largest' and update if a bigger one is found
        largest = max(largest, arr[i])

    # Print the largest element found in the array
    print(f"The large Element is : {largest}")


def second_large(arr):
    # Initialize both 'largest' and 'second_largest' with very small values
    # (Negative infinity ensures any element will be greater)
    largest = float("-inf")
    second_largest = float("-inf")
    
    # Get the length of the array
    n = len(arr)
    
    # Loop through the array elements
    for i in range(0, n):
        # If the current element is greater than 'largest',
        # move the previous 'largest' to 'second_largest'
        # and update 'largest' with the new biggest element
        if arr[i] > largest:
            second_largest = largest
            largest = arr[i]
        # If current element is smaller than 'largest' but greater than 'second_largest',
        # and it's not equal to 'largest', update 'second_largest'
        elif arr[i] > second_largest and arr[i] != largest:
            second_largest = arr[i]
    
    # Print both largest and second largest elements
    print("Largest element:", largest)
    print("Second largest element:", second_largest)


def sorted_array(arr):
    # Get the length of the array
    n = len(arr)
    
    # Traverse the array and check each consecutive pair
    for i in range(0, n-1):
        # If the current element is greater than the next one,
        # then the array is not sorted in ascending order
        if arr[i] > arr[i+1]:
            print("The Array is not Sorted")
            break
    
    # This print will always execute (even if the array was not sorted)
    # — if you want it to print only when sorted, handle it differently
    print("The Array is Sorted")


# Sample array for testing
arr = [3, 5, 7, 9, 15, 16, 17]

# Function calls
second_large(arr)   # Find and print largest & second largest
large_element(arr)  # Find and print only the largest
sorted_array(arr)   # Check if the array is sorted
