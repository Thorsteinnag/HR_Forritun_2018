# Find the maximum positive integer input by a user.  
# The user repeatedly inputs numbers until a negative value is entered.

# While the number that the user inputs is larger than zero, keep going, otherwise break.
# If the number that the user inputs is larger than the existing numbers already entered,
# then that number will be the maximum.

num_int = int(input("Input a number: "))    # Do not change this line

max_int = 0

while num_int >= 0:    
    if num_int > max_int:
        max_int = num_int

    num_int = int(input("Input a number: "))

    if num_int < 0:
        break

print("The maximum is", max_int)    # Do not change this line