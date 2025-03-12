# Prog01: Create a program that ask user to input 10 numbers. Display all numbers that have duplicate.

# initialize an empty list to store user input
list_numbers = []

# ask user to input 10 numbers
for i in range(10):
    number = float(input(f"Number {i+1}: "))
    list_numbers.append(number)

# find and display numbers that have duplicates
duplicate_numbers = []
for number in list_numbers:
    if list_numbers.count(number) > 1 and number not in duplicate_numbers:
        duplicate_numbers.append(number)

# display the result
print("Numbers with duplicates:", duplicate_numbers)