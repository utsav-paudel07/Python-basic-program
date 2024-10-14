# Get a series of numbers from the user
numbers = input("Enter numbers separated by spaces: ")

# Convert the input string to a list of integers
numbers_list = [int(num) for num in numbers.split()]

# Initialize counters
even_count = 0
odd_count = 0

# Count even and odd numbers
for num in numbers_list:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

# Print the results
print("Number of even numbers:", even_count)
print("Number of odd numbers:", odd_count)
