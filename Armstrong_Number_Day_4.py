# START
#   INPUT number
#   SET sum = 0
#   SET temp = number
#   CALCULATE n = number of digits in number

#   WHILE temp > 0 DO
#     digit = temp MOD 10
#     sum = sum + (digit ^ n)
#     temp = temp DIV 10
#   END WHILE

#   IF sum == number THEN
#     PRINT "Armstrong number"
#   ELSE
#     PRINT "Not an Armstrong number"
#   END IF
# END

number = int(input("Enter a Number : "))
sum = 0
temp = number
n = len(str(number))

while temp > 0:
    last_digit = temp % 10
    sum = sum + (last_digit ** n)
    temp = temp // 10

if ( sum == number):
    print ("Armstrong Number")
else:
    print("Not an Armstrong Number")