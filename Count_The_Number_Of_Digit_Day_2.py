# You have integer n and you have to count the total number of digits in it
# example -:
# input n = 4574 then answer will be count = 4

from math import *

def CountDigits( n):
    return int(log10(n)) + 1

a = int(input("Enter your number "))
answer = CountDigits(a)

print(f"Total number of digit in {a} is {answer}")