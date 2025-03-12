# Prog08: Create a program that ask user to input 10 numbers. Print how many are odd numbers.

'''
    initialize the odd_numbers container to 0
    use for loop with range 10
        ask user to input 10 numbers
        use if statement to determine whether the number is odd or not
            add 1 to odd_numbers if the number input is an odd number
    print how many odd numbers are input
'''
# initialize odd_numbers container to 0
odd_numbers = 0

# use for loop with range 10
for i in range(10):

    # ask user to input 10 numbers
    number = float(input(f"Number {i+1}: "))

    # use if statement to determine whether a number is odd or not
    if number % 2 != 0:

        # add 1 to odd_numbers if the number input is an odd number
        odd_numbers += 1