def sum_of_digit(num, total):
    print(f"Num : {num}, Total : {total}")
    if num == 0:
        return total
    last = num % 10
    total = total + last
    return sum_of_digit(num // 10, total)

num = 3656
total = 0

total = sum_of_digit(num, total)

print(f"The sum of total is : {total}")

#function to reverse an list/array using recursion
def func(l, i, j):
    if i >= j:
        return
    l[i], l[j] = l[j], l[i]
    func(l, i + 1, j - 1)

l = [1, 2, 3, 4, 5]
func(l, 0, len(l) - 1)
print(*l)