# Prog06: Create a program that ask user to input 2 numbers. Print the result when the first number is raised to the second number.

'''
    ask the user to input first_number and second_number
    print exponent
'''
# ask the user to input first_number and second_number
first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))

# print the exponent
print(first_number, "raised to", second_number, "is", first_number ** second_number)