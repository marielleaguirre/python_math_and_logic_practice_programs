# Prog02: Create a program that ask user to input 2 numbers. Print "Not Equal" when the numbers are not the same.

'''
    ask user to input the first_number and second_number
    use if statement to determine if the two numbers are not equal
'''
# ask the user to input first_number and second_number
first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))

# use if statement to determine if the two numbers are not equal and print Not Equal
if first_number != second_number:
    print("The numbers are Not Equal.")