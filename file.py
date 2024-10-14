num = int(input("Enter the number: "))
filename = "Product.txt"

with open(filename, "w") as file:
    for i in range(1, 11):
        product = num * i
        # Print the result to the console
        print(f"The product of {num} x {i} is: {product}")
        
        # Write the result to the file
        file.write(f"The product of {num} x {i} is: {product}\n")
