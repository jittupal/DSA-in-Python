arr = [1, 2, 3, 1, 1, 2, 3, 4, 4, 1, 5, 5, 5]

ans = 0
for num in arr:
    ans = ans^num
print(ans)