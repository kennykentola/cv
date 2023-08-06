'''def is_armstrong_number(number):
    # Convert the number to a string to iterate over its digits
    num_str = str(number)
    
    # Calculate the sum of the digits raised to the power of the total number of digits
    digit_sum = sum(int(digit) ** len(num_str) for digit in num_str)
    
    # Check if the sum is equal to the original number
    if digit_sum == number:
        return True
    else:
        return False

# Test the function
number = 371
if is_armstrong_number(number):
    print(number, "is an Armstrong number.")
else:
    print(number, "is not an Armstrong number.")
'''

'''def is_armstrong_number(number):
    num_str = str(number)
    digit_sum = sum(int(digit) ** len(num_str) for digit in num_str)
    if digit_sum == number:
        return True
    else:
        return False

# Ask the user to input a number
number = int(input("Enter a number: "))

# Check if the number is an Armstrong number
if is_armstrong_number(number):
    print(number, "is an Armstrong number.")
else:
    print(number, "is not an Armstrong number.")'''




def is_armstrong_number(number):
    num_str = str(number)
    digit_sum = sum(int(digit) ** len(num_str) for digit in num_str)
    if digit_sum == number:
        return True
    else:
        return False

while True:
    # Ask the user to input a number
    number = int(input("Enter a number (or enter 0 to exit): "))

    if number == 0:
        break

    # Check if the number is an Armstrong number
    if is_armstrong_number(number):
        print(number, "is an Armstrong number.")
    else:
        print(number, "is not an Armstrong number.")









