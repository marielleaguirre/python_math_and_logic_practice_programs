# Prog04: Create a program that ask user to input a number, continue asking until the user input is invalid. 
# Display the number from highest to lowest. Clue: sort() function

# initialize an empty list to store user input
list_numbers = []

# continuously prompts the user to input a number
while True:
    try:
        # take user input
        number = float(input("Enter a number: "))  
        list_numbers.append(number)  # add the number to the list
    except ValueError:
        print("Invalid Input. Now sorting in descending order...")
        # stop asking for input when non-numeric value is entered
        break
    
# sort and display the list of number if the list is not empty
# sort the list in descending order