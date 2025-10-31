def rearrange(arr):
    # Step 1: Get the total number of elements in the array
    n = len(arr)
    
    # Step 2: Create two lists to store positive and negative numbers separately
    pos = []  # will hold positive numbers
    neg = []  # will hold negative numbers
    
    # Step 3: Traverse the array and separate positive and negative elements
    for i in range(n):
        if arr[i] >= 0:
            pos.append(arr[i])   # Add positive numbers to pos[]
        else:
            neg.append(arr[i])   # Add negative numbers to neg[]
    
    # Step 4: Initialize indices for merging
    i = 0             # index for main array (arr)
    pos_index = 0     # index for pos[]
    neg_index = 0     # index for neg[]
    
    # Step 5: Place elements alternately from pos[] and neg[]
    # Continue until one of them runs out
    while pos_index < len(pos) and neg_index < len(neg):
        arr[i] = pos[pos_index]     # place next positive
        pos_index += 1
        i += 1
        
        arr[i] = neg[neg_index]     # place next negative
        neg_index += 1
        i += 1
    
    # Step 6: If any positive numbers remain, place them at the end
    while pos_index < len(pos):
        arr[i] = pos[pos_index]
        pos_index += 1
        i += 1
    
    # Step 7: If any negative numbers remain, place them at the end
    while neg_index < len(neg):
        arr[i] = neg[neg_index]
        neg_index += 1
        i += 1
    
    # Step 8: Print the rearranged array
    print(*arr)


# ✅ Test Case 1
# Contains both positive and negative numbers
# Expected output: starts with positive and alternates
arr = [3, 5, 6, 7, -1, 4, -3, -5, -6, -3, -2]
rearrange(arr)  
# Output example: 3 -1 5 -3 6 -5 7 -6 4 -3 -2

# ✅ Test Case 2
# Contains only negative numbers
# Since there are no positives, array remains as is
arr = [-3, -4, -6, -6, -2, -1, -8]
rearrange(arr)
# Output: -3 -4 -6 -6 -2 -1 -8
