# Create a program that ask the user to input their fullname in incorrect casing. 
# Print the input in snake case.
# Example:
# Input: jUAn DEla CrUZ
# Output: juan_dela_cruz

# ask the user to input their full name in incorrect casing
full_name = input("Enter your full name in incorrect casing: ")

# use lower() method to convert the string to lowercase then replace() method to replace spaces with underscores
snake_case_name = full_name.lower().replace(" ", "_")

# print the full name in snake case
print("Full name (in snake_case):", snake_case_name)