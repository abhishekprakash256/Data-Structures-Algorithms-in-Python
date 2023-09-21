"""
The question is to find the happy number by squared 
and not have a cycle and return 1 at a point 

example 
28 = 68
68 = 100 
100 = 1

so 28 is a happy number 
"""

#---------------------------optimize approach ----------------------------------

from happy_number import * 


def sum_of_squared_digits(number):  # Helper function that calculates the sum of squared digits.
    
    total_sum = 0
    i = 0

    while number > 0:
        digit = number % 10

        number = number // 10

        total_sum = total_sum + digit ** 2

    return total_sum

print(sum_of_squared_digits(90))