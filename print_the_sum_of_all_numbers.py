# Prog07: Create a program that ask user to input 10 numbers. Print the sum of all the numbers.

'''
    initialize total_sum to 0
    use for loop with a range of 10
        ask the user to input 10 numbers
        add number to total_sum
    print the sum of all numbers
'''
# initialize total_sum to 0
total_sum = 0

# use for loop with a range of 10
for i in range(10):
    
    # ask the user to input 10 numbers
    number = float(input(f"Number {i+1}: "))

    # add the number to total_sum
    total_sum += number