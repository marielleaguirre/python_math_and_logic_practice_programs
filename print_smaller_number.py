# Prog01: Create a program that ask user to input 2 numbers. Print the smaller number.

'''
    ask user to input the first_number and second_number
    if first_number is less than second_number then
        print first_number
    else
        print second_number
'''
# ask the user to input two numbers
first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))

# use if-else statement to determine the smaller number
if first_number < second_number:
    print("Smaller Number:", first_number)
else:
    print("Smaller Number:", second_number)