# Time Complexity -: It is the time which calculated by an algorithm as it's input size increases.
# We calculate time complexity in a mathematical expression instead of seconds or minutes as the input size grows.
# It is denoted by Big O notation.

#Example -:
# Let's say we have an array of n elements and we want to find a specific element in the array.
# We can use a linear search algorithm to find the element. The time complexity of this algorithm is O(n) because in the worst case, we may have to check all n elements in the array to find the specific element.
# For i in range(n):
#     if arr[i] == target:  # O(n)
#         return i  # O(1)              
# return -1  # O(1)
# The overall time complexity of this algorithm is O(n) + O(1) + O(1) = O(n).       
# As the input size n increases, the time taken by the algorithm to find the element also increases linearly.
# Therefore, we say that the time complexity of the linear search algorithm is O(n).

#Example -:
# For i in range(1, n):  # O(n)
#    For j in range(n):  #O(n)
#        Print(j)    #O(1)
# So it's Time complexity will be O(n) * O(n) *O(1) = O(n^2)

# Space Complexity -: 
# It is the total memory used by an algorithm as input size increases.

# It has 2 parts:
# 1. Input Space     → Memory needed to store the input data
# 2. Auxiliary Space → Extra memory used by the algorithm 
#                      (like variables, temporary arrays, recursion stack)

# ---------------------------------------------------
# Example 1: Constant Space - O(1)
# ---------------------------------------------------
def add_numbers(a, b):
    result = a + b   # only one variable
    return result

# Input Space     → a, b (2 inputs)
# Auxiliary Space → result (1 variable)
# Total Space     → Constant → O(1)


# ---------------------------------------------------
# Example 2: Linear Space - O(n)
# ---------------------------------------------------
def make_list(n):
    arr = []         # empty list
    for i in range(n):
        arr.append(i)
    return arr

# Input Space     → n
# Auxiliary Space → arr of size n
# Total Space     → O(n)