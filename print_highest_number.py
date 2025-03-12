# Prog03: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the highest number

# initialize an empty list to store user input
highest_number = []

# continuously prompts the user to input a number
while True:
    try:
        # take user input
        number = float(input("Enter a number: "))
        highest_number.append(number)  # add the number to the list
    except ValueError:
        # stop asking for input when non-numeric value is entered
        break
    
# display the highest number if the list is not empty
