# Prog04: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the lowest number

# initialize an empty list to store user input
lowest_number = []

# continuously prompts the user to input a number
while True:
    try:
        # take user input
        number = float(input("Enter a number: "))
        lowest_number.append(number)  # add the number to the list
    except ValueError:
        # stop asking for input when non-numeric value is entered
        break
    
# display the lowest umber if the ist is not empty
