# Prog02: Create a program that ask user to input 2 numbers. Print "Equal" when the numbers are the same.

'''
    ask the user to input first_number and second_number
    if first_number is equals to second_number then
        print Equal
'''
# ask the user to input first_number and second_number
first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))

# use if statement to determine if the two numbers are equal then print Equal
if first_number == second_number:
    print("The numbers are Equal.")