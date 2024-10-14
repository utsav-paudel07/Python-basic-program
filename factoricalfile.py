num = int(input("Enter the number: "))
filename = "factorial.txt"

with open(filename, "w") as file:
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    print('The factorial of the number is: ', fact)
    file.write(f"The factorial of the number {num} is {fact}")

