# Prog06: Create a program that ask user to input 10 numbers. Print the result of the first number minus all of the remaining numbers.

'''
    initialize total_difference container to 0
    use for loop with range 10
        ask the user to input 10 numbers
        if the iteration is equals to 0 then (the first number input)
            add the number input to the total_difference
        else (the remaining numbers)
            subtract the number input to the total_difference
    print the total_difference
'''
# initialize total_difference container to 0
total_difference = 0

# use for loop with range 10
for i in range(10):

    # ask the user to input 10 numbers
    number = float(input(f"Number {i+1}: "))

    # use if statement to determine if the iteration is equals to 0 (it is the first number)
    if i == 0:

        # add the first number input to the total_difference
        total_difference += number

    # else (the remaining numbers)
    else:

        # subtract the number input to the total_difference
        total_difference -= number

# print the total_difference
print("The difference is equals to", total_difference)