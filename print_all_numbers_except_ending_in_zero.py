# Prog10: Create a program that print all the numbers starting from 0 to 100 except numbers ending in zero.

'''
    loop through number from 0 to 100
        check if number is not a multiple of 10 (if number divided by 10 has a remainder)
            print all the numbers except ending in zero
'''
# use for loop with range of 101
for number in range(101):

    # check if number is not multple of 10
    if number % 10 != 0:

        # print all the numbers that is not ending in zero
        print(number)