# Prog01: Create a program that ask user to input 2 numbers. Print the bigger number.

'''
    ask the user to input first_number and second_number
    if first_number is greater than second_number then
        print first_number
    else
        print second_number
'''
# ask the user to input first_number and second_number
first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))

# use if-else statement to determine the bigger number
if first_number > second_number:
    print("Bigger Number:", first_number)
else:
    print("Bigger Number:", second_number)