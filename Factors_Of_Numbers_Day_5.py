# INPUT N

# CREATE empty list result

# SET sqr = integer value of square root of N

# FOR i FROM 1 TO sqr INCLUSIVE:
#     IF N MOD i == 0 THEN
#         ADD i to result
#         IF (N / i) != i THEN
#             ADD (N / i) to result

# SORT result in ascending order

# FOR each number num in result:
#     PRINT num followed by a space





from math import sqrt

# Input a number
N = int(input("Enter a number: "))

# Find divisors
result = []
sqr = int(sqrt(N))

for i in range(1, sqr + 1):
    if N % i == 0:
        result.append(i)
        if N // i != i:  # avoid duplicate for perfect squares
            result.append(N // i)

# Sort and print in one line
result.sort()
for num in result:
    print(num, end=" ")
