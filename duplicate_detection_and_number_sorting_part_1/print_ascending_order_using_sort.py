# Prog05: Create a program that ask user to input a number, continue asking until the user input is invalid. 
# Display the number from lowest to highest. Clue: sort() function

# initialize an empty list to store user input
list_numbers = []

# continuously prompts the user to input a number
while True:
    try:
        # take user input
        number = float(input("Enter a number: "))
        list_numbers.append(number)  # add the number to the list
    except ValueError:
        print("Invalid Input. Now sorting in ascending order...")
        # stop asking for input when non-numeric value is entered
        break

# sort and display the list of numbers if the list is not empty
if list_numbers:
    list_numbers.sort()  # sort the list in ascending order
    print("Number from lowest to highest", list_numbers)
else: 
    print("No numbers were entered.")