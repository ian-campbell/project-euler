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


def find_millionth_perm(sequence, permutation_number):

    # Create a mutable list of the sequence of numbers
    numbers_list = list(sequence)

    # Create an empty list in which to store the final answer
    final_answer = []
    
    while len(numbers_list):

        # On the first loop this is 9! which is 362,880
        my_factorial = math.factorial(len(numbers_list)-1)

        # Find the next number of the final answer
        digit = permutation_number / my_factorial

        # Update the permutation 
        permutation_number = permutation_number % my_factorial

        # Update the final answer
        final_answer.append(numbers_list[digit])

        # Update the working list of numbers
        numbers_list = numbers_list[0:digit] + numbers_list[digit+1:]

    return final_answer

print find_millionth_perm(range(0,10), 999999)







