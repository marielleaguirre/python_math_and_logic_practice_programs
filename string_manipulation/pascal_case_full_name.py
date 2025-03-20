# Create a program that ask the user to input their fullname in incorrect casing. 
# Print the input in pascal case.
# Example:
# Input: jUAn DEla CrUZ
# Output: JuanDelaCruz

# ask th user to input their name in incorrect casing
full_name = input("Enter your full name in incorrect casing: ")

# use title() method to convert input to proper casing then replace() method to remove the spaces
pascal_case_name = full_name.title().replace(" ", "")

# print the full name in pascal case
print("Full name (in PascalCase):", pascal_case_name)