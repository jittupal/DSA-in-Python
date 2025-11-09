def three_sum(arr):
    # Find all unique triplets in `arr` that sum to zero and print them.
    # Approach:
    # 1. Sort the array to make duplicate handling and two-pointer scanning easier.
    # 2. Fix one element (arr[i]) and use two pointers (j, k) to find pairs such that
    #    arr[i] + arr[j] + arr[k] == 0.
    # 3. Skip duplicates for i, j and k to ensure unique triplets.
    n = len(arr)
    ans = []

    # Sorting lets us move pointers deterministically and skip duplicates.
    arr.sort()

    # Edge guard: if array has fewer than 3 elements, no triplet possible
    if n < 3:
        print(*ans)
        return

    # Iterate over each index i as the first element of potential triplet
    for i in range(n):
        # Skip duplicate values for i to avoid repeated triplets
        if i != 0 and arr[i] == arr[i-1]:
            continue

        # Two-pointer initialization:
        j = i + 1        # left pointer starts just after i
        k = n - 1        # right pointer starts at end of array

        # Move pointers inward to find pairs that sum with arr[i] to zero
        while j < k:
            total_sum = arr[i] + arr[j] + arr[k]

            if total_sum < 0:
                # Sum too small -> need larger value -> move left pointer right
                j += 1
            elif total_sum > 0:
                # Sum too large -> need smaller value -> move right pointer left
                k -= 1
            else:
                # Found a valid triplet
                temp = [arr[i], arr[j], arr[k]]
                ans.append(temp)

                # Move both pointers to continue searching for other pairs
                j += 1
                k -= 1

                # Skip duplicates for j (move j forward past equal values)
                while j < k and arr[j] == arr[j-1]:
                    j += 1
                # Skip duplicates for k (move k backward past equal values)
                while j < k and arr[k] == arr[k+1]:
                    k -= 1

    # Print all unique triplets found
    print(*ans)


# Example usage (unsorted input; function sorts internally)
arr = [1, -1, 0, 3, 2, -2, 0, 1, -1, -3, 0, -4, 4, 0]

three_sum(arr)