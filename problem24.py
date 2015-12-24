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

# create a list
list_of_numbers = list(sequence)
working_tally = 0
current_factorial = 10

def find_millionth_perm(working_tally, current_factorial):

    if working_tally == 1000000:
        return None
    
    # make a variable to keep track of how close we are to 1 million


    # make a variable to keep track of which factorial we are on


    x = current_factorial
    x -=1
    p = 10 - current_factorial

    myfact = math.factorial(x)

    test_tally = working_tally + myfact

    if test_tally > end_point:
        pass
    else:
        working_tally = test_tally

    list_of_numbers[p], list_of_numbers[p+1] = list_of_numbers[p+1], list_of_numbers[p]
   


    print list_of_numbers
    print working_tally





        
        # break

    # while working_tally < end_point:
    #     find_millionth_perm(working_tally)




find_millionth_perm(working_tally, current_factorial)

