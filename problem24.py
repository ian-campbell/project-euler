import math


# A permutation is an ordered arrangement of objects.
# For example, 3124 is one possible permutation of the
# digits 1, 2, 3 and 4. If all of the permutations are
# listed numerically or alphabetically, we call it
# lexicographic order. The lexicographic permutations
# of 0, 1 and 2 are:
# 012   021   102   120   201   210
# What is the millionth lexicographic permutation
# of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?


sequence = '0123456789'
end_point = 1000000

# create a list of the numbers ['0','1','2'...]
list_of_numbers = list(sequence)

# set a variable to store the running tally of permutations
perm_tally = 0

# set a variable to store the current factorial number
current_factorial = 10

# define a recursive function
def find_millionth_perm(perm_tally, current_factorial, list_of_numbers):

    if perm_tally == 1000000:
        print "one"
    
    
    p = 10 - current_factorial

    myfact = math.factorial(x)

    test_tally = perm_tally + myfact

    if test_tally > end_point:
        x = current_factorial
        x -=1
    else:
        perm_tally = test_tally


        #this is where i'm stuck, how to update the number
    list_of_numbers[p], list_of_numbers[p+1] = list_of_numbers[p+1], list_of_numbers[p]
    


find_millionth_perm(perm_tally, current_factorial, list_of_numbers)

