def merge_sorted_lists(list1, list2):
    i, j = 0, 0
    merged = []

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            if not merged or merged[-1] != list1[i]:
                merged.append(list1[i])
            i += 1
        elif list1[i] > list2[j]:
            if not merged or merged[-1] != list2[j]:
                merged.append(list2[j])
            j += 1
        else:
            # Equal elements — add only once
            if not merged or merged[-1] != list1[i]:
                merged.append(list1[i])
            i += 1
            j += 1

    # Add remaining elements (if any)
    while i < len(list1):
        if not merged or merged[-1] != list1[i]:
            merged.append(list1[i])
        i += 1

    while j < len(list2):
        if not merged or merged[-1] != list2[j]:
            merged.append(list2[j])
        j += 1

    return merged


# Example usage
list1 = [1, 3, 5, 7]
list2 = [2, 3, 5, 8, 9]
result = merge_sorted_lists(list1, list2)
print(result)   # Output: [1, 2, 3, 5, 7, 8, 9]
