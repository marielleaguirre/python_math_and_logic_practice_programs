# Create a program that ask the user to input a complete statement. 
# Print the number of words in the input.
# Example:
# Input: We will weather the weather whatever the weather whether we like it or not
# Output: 14

# ask user to input a complete statement
complete_statement = input("Enter a complete statement: ")

# use split() method to split the words in the statement then len() method for counting the number of words
words_in_statement = len(complete_statement.split())

# print the number of words in the statement