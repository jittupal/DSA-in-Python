def decimalToBinary(n):
    result = ""
    a = n
    while n > 0:
        if n % 2 == 1:
            result += "1"
        else:
            result += "0"
        n = n // 2
    result = result[::-1]
    
    print(f"The Binary Of {a} ::  ", result)
    
# def BinaryToDecimal(s):
    
decimalToBinary(17)
decimalToBinary(27)
decimalToBinary(77)
decimalToBinary(12)
decimalToBinary(67)