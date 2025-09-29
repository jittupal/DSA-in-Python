#We have a list of numbers, we need to store it in hash

nums = [1,2, 4, 6, 8,9, 1, 2, 4, 9, 5, 3]

n = len(nums)

hash_table = {}
for i in range(0, n):
    hash_table[nums[i]] = hash_table.get(nums[i], 0) + 1

print(*hash_table)


print(hash_table.get(nums[1], 0))