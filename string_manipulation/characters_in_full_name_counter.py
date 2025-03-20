# Create a program that ask the user to input their fullname. 
# Print the number of characters in the input.
# Example:
# Input: Juan Dela Cruz
# Output: 14

# ask the user to input their full name
full_name = input("Enter your full name: ")

# use len() method to count the number of characters in the user input
characters_count = len(full_name)

# print the number of characters in the full name
print("Total number of characters in the full name:", characters_count)