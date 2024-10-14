user_input = input("Enter number/words: ")
reversed_input = user_input[::-1]

if reversed_input == user_input:
    print("Palindrome")

else:
    print("Not palindrome")