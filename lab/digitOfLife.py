# the digit of life is the sum of the digits of the birthdate. 
# write a function that takes a birthdate and returns the digit of life. ✅
# if the sum has more than one digit, repeat the process until a single digit is reached.✅
# Challenge: use recursion to solve the problem.✅

birthdate = input("Enter your birthdate in the format YYYYMMDD: ")

def digitOfLife(date):
    sum = 0
    nums = list(str(date))
    for digit in nums:
        sum += int(digit)
    if len(str(sum))> 1:
        sum = digitOfLife(sum)
    return sum


print(digitOfLife(birthdate))