# Prog03: Create a program that ask user to input a number
# continue asking until the user input is invalid. 
# Display "Unique" after input when the inputted number don't have duplicate. 
# Display "Duplicate" after input when the inputted number have duplicate.

# initialize an empty list to store user input
list_numbers = []

# continuously prompts the user to input a number
while True:
    try:
        # take user input
        number = float(input("Enter a number: "))
        
        # check if the number alreasy exists in the list
        if number in list_numbers:
            print(number, "is a DUPLICATE.")  # display "Duplicate" if the number already exists
        else:
            print(number, "is UNIQUE.")  # display "Unique" if it is a new number
            list_numbers.append(number)  # add the number to the list
            
    except ValueError:
        # stop asking for input when non-numeric value is entered 
        print("Invalid input detected. Program stopped.")
        break