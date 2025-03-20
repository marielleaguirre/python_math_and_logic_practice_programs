# Create a program that ask the user to input their fullname in incorrect casing. 
# Print the input in proper casing.
# Example:
# Input: jUAn DEla CrUZ
# Output: Juan Dela Cruz

# ask the user to input their full name in incorrect casing
full_name = input("Enter your full name in incorrect casing: ")

# use title() method to convert input to title case
proper_casing_name = full_name.title()

# print the full name in proper casing
print("Full name (proper casing):", proper_casing_name)