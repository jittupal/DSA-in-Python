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