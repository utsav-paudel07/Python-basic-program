# Program to find numbers divisible by 7 and are multiples of 5 between 1500 and 2700

# Loop through the range
for num in range(1500, 2701):
    if num % 7 == 0 and num % 5 == 0:
        print(num)
