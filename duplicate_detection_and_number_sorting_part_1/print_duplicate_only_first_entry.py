# Prog02: Create a program that ask user to input 10 numbers. Display all numbers. For numbers with duplicate, display only the first entry.

# initialize an empty list to store user input
list_numbers = []

# ask user to input 10 numbers
for i in range(10):
    number = float(input(f"Number {i+1}: "))  # take input as integer
    if number not in list_numbers:  # only store the first entry
        list_numbers.append(number)

# display the result
print("All numbers (first entry of duplicates only):", list_numbers, end=" ")
