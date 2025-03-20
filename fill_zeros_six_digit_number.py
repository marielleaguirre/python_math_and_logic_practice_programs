# Create a program that ask the user to input a number (0-1000). 
# Print the number in 6 digit format. Add zeros at the beginning to complete the 6 digit.
# Example:
# Input: 143
# Output: 000143

# ask user to input a number from 0 to 1000
input_number = input("Enter a number from 0 to 1000: ")

# use zfill() method to fill the beginning with zeroes to make a 6-digit format number
fill_zeros = input_number.zfill(6)

# print the input in 6-digit format