# Create a program that ask the user to input their fullname.
# Print the input in all capital letter.
# Example:
# Input: Juan Dela Cruz
# Output: JUAN DELA CRUZ

# ask the user to input their full name
full_name = input("Enter your full name: ")

# use upper() method to turn all the characters of the full name to uppercase
upper_case_name = full_name.upper()

# print the full name in uppercase
print("Full name (in UPPERCASE):", upper_case_name)