# Create a program that ask the user to input their fullname with several space characters at the beginning. 
# Print the input without the spaces in the beginning.
# Example:
# Input:         Juan Dela Cruz
# Output: Juan Dela Cruz

# ask user to input their full name with several spaces in the beginning
full_name = input("Enter your full name (with several spaces at the beginning): ")

# use lstrip() method to remove left padded spaces
remove_leading_spaces = full_name.lstrip()

# print the full name without the spaces at the beginning
print("Full name (no leading spaces):", remove_leading_spaces)