list = input("Enter the number/name: ")
copy_list = list.copy()
copy_list.reverse()

if (copy_list == list):
    print("Palindrome")

else:
    print("Not palindrome")