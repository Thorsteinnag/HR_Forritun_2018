# Design an algorithm that generates the first n numbers in the following sequence:; 1, 2, 3, 6, 11, 20, 37, ___, ___, ___, …

# The first numbers in the sequence are always 1, 2, 3,
# The fourth number is 6, the sum of the first three numbers
# The fifth number is 11, the sum of the three numbers infront 2,3,6 and so on.
# n4 = n3 + n2 + n1 

n = int(input("Enter the length of the sequence: ")) # Do not change this line

first_num = 1
second_num = 2
third_num = 3

next_num = 0

# We always need to have 1, 2, and 3. As long as the input is greater than 1,2, or 3 we print them.
if n >= 1:
    print(first_num)

if n >= 2:
    print(second_num)

if n >= 3:
    print(third_num)

# we have already counted the first three numbers, that is why we use range(n-3).
if n > 3:
    for seq in range(n-3):
        next_num = first_num + second_num + third_num  # this is the formula

        #then we need to change the first three numbers 
        first_num = second_num
        second_num = third_num
        third_num = next_num

        print(next_num)
