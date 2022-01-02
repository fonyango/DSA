
# Data Structures and Algorithms

"""
-- Sum of two positive integers

Create a function that returns the sum of the two lowest positive numbers given an array of minimum 4 positive integers. No floats or non-positive integers will be passed.

For example, when an array is passed like [19, 5, 42, 2, 77], the output should be 7.

[10, 343445353, 3453445, 3453545353453] should return 3453455.
"""

def sum_two_smallest_numbers(numbers):

    # sort the values in ascending order
    numbers.sort(reverse=True)

    x = numbers[-1]
    y = numbers[-2]

    return x + y

numbers = [5, 8, 12, 18, 22]
print(sum_two_smallest_numbers(numbers))

#------------------------------------------------------
"""
Given the triangle of consecutive odd numbers:

             1
          3     5
       7     9    11
   13    15    17    19
21    23    25    27    29
...
Calculate the sum of the numbers in the nth row of this triangle (starting at index 1) e.g.: (Input --> Output)
"""

def row_sum_odd_numbers(n):

    num_sum = n **3

    return num_sum

print(row_sum_odd_numbers(13))
print(row_sum_odd_numbers(29))

# -------------------------------------------------------------------

"""
Create a function that takes a list of non-negative integers and strings and returns a new list with the strings filtered out.
"""
def filter_list(my_list):
    num_list = []
    for i in my_list:
        if isinstance(i, int) == True:
            num_list.append(i)
        else:
            pass
    return num_list

print(filter_list([1,2,'a','b']))