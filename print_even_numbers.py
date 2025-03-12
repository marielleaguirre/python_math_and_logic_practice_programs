# Prog07: Create a program that ask user to input 10 numbers. Print how many are even numbers.

'''
    initialize even_numbers container to 0
    use for loop with range of 10
        ask the user to input 10 numbers
        if the number divided by 2 has 0 remainder then
             increment even_numbers by 1
    print the total of even numbers
'''
# initialize even_numbers container to 0
even_numbers = 0

# use for loop with range 10
for i in range(10):

    # ask the user to input 10 numbers
    number = float(input(f"Number {i+1}: "))

    # if the number input divided by 2 has 0 remainder
    if number % 2 == 0:

        # increment even_numbers by 1
        even_numbers += 1