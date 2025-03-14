# Prog10: Create a program that ask user to input 2 numbers. Print all the numbers between the two numbers.

'''
    ask the user to input the first_number and second_number
    check if first_number is greater than second_number
        swap the values of first_number and second_number (to ensure proper order)
    loop through numbers from first_number plus 1 to second_number
        print each number between the range
'''
# ask the user to input first_number and second_number
first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))

# check if first_number is greater than second_number
if first_number > second_number:

    # swap the values of the two numbers to ensure proper order
    first_number, second_number = second_number, first_number

# use for loop, start from first_number + 1 stop to second_number
for i in range(first_number + 1, second_number):

    # print each number between the range
    print(i)