def solve(index, digits, char_map, subset, result):
    # Base case: all digits processed
    if index == len(digits):
        result.append("".join(subset))
        return

    current_digit = digits[index]
    possible_letters = char_map[current_digit]

    # Loop inside recursion
    for ch in possible_letters:
        subset.append(ch)                 # choose
        solve(index + 1, digits, char_map, subset, result)  # explore
        subset.pop()                      # backtrack


def letterCombinations(digits):
    if not digits:
        return []

    char_map = {
        '2': "abc", '3': "def", '4': "ghi", '5': "jkl",
        '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"
    }

    result = []
    subset = []

    solve(0, digits, char_map, subset, result)
    print(result)

letterCombinations('23')