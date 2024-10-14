def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


number = int(input("Enter the number whose factorial is to be calculated: "))

result = factorial(number)
print(f"The factorial of {number} is {result}.")
