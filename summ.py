def sum_of_digits(n):
    # Base case: If the number is a single digit, return that digit
    if n == 0:
        return 0
    # Recursive case: Add the last digit to the sum of the remaining digits
    else:
        return n % 10 + sum_of_digits(n // 10)

# Get user input
number = int(input("Enter a number: "))

# Make sure to handle negative numbers


print(f"The sum of digits of {number} is {sum_of_digits(number)}")
