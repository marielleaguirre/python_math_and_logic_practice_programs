# Prog01: Create a program that ask user to input 10 numbers. Display all numbers that don't have duplicate.

# initialize an empty list to store user input
list_numbers = []

# ask user to input 10 numbers
for i in range(10):
    number = float(input(f"Number {i+1}: "))
    list_numbers.append(number)

# find and display numbers that are not duplicated
unique_numbers = []
for number in list_numbers:
    if list_numbers.count(number) == 1:  # if the count of the number is 1, it is unique
        unique_numbers.append(number)

# display the result
print("Unique numbers:", unique_numbers)