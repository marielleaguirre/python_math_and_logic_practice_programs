# Prog05: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the average.

# initialize an empty list to store user input
list_numbers = [] 

# continuously prompts the user to input a number
while True:
    try:
        # take user input
        number = float(input("Enter a number: "))
        list_numbers.append(number)  # add the number to the list
    except ValueError:
        # stop asking for input when non-numeric value is entered
        break
    
# calculate and display the average of the numbers that were entered