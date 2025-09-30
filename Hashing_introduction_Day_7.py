def checkEqual(a, b) -> bool:
    # Step 1: If lengths differ, lists can't be equal
    if len(a) != len(b):
        return False

    # Step 2: Build frequency hash table for list a
    hash_tab = {}
    for num in a:
        hash_tab[num] = hash_tab.get(num, 0) + 1
    # Example: a = [1, 2, 3, 2]
    # hash_tab = {1: 1, 2: 2, 3: 1}

    # Step 3: Check elements of list b
    for num in b:
        if num not in hash_tab:  # element not present in a
            return False
        if hash_tab[num] == 0:  # element count already used up
            return False
        hash_tab[num] -= 1      # use one occurrence

    # Step 4: If all checks passed, lists are equal
    return True


# -------------------------
# 🔹 Dry Run Example 1 (Equal lists)
a = [1, 2, 3, 2]
b = [2, 3, 2, 1]
print(checkEqual(a, b))  # ✅ True

# 🔹 Dry Run Example 2 (Not equal lists)
a = [1, 2, 3]
b = [1, 2, 2]
print(checkEqual(a, b))  # ❌ False
