"""
Given an array of integers, find the one that appears an odd number of times.

There will always be only one integer that appears an odd number of times.

Examples
[7] should return 7, because it occurs 1 time (which is odd).
[0] should return 0, because it occurs 1 time (which is odd).
[1,1,2] should return 2, because it occurs 1 time (which is odd).
[0,1,0,1,0] should return 0, because it occurs 3 times (which is odd).
[1,2,2,3,3,3,4,3,3,3,2,2,1] should return 4, because it appears 1 time (which is odd).

"""

def find_it(Seq):
    # count all the unique integers and save them as key-value pairs
    my_dict = {i:Seq.count(i) for i in Seq}

    # iterate through the dict and find the key whose value is an odd number
    for key, value in my_dict.items():
        if value % 2 != 0:
            return key

print(find_it([1,2,2,3,3,3,4,3,3,3,2,2,1]))
print(find_it([0,1,0,1,0]))

#  --------------------------------------------------------------
"""
In a factory a printer prints labels for boxes. For one kind of boxes the printer has to use colors which, for the sake of simplicity, are named with letters from a to m.

The colors used by the printer are recorded in a control string. For example a "good" control string would be aaabbbbhaijjjm meaning that the printer used three times color a, four times color b, one time color h then one time color a...

Sometimes there are problems: lack of colors, technical malfunction and a "bad" control string is produced e.g. aaaxbbbbyyhwawiwjjjwwm with letters not from a to m.

You have to write a function *printer_error* which given a string will return the error rate of the printer as a string representing a rational whose numerator is the number of errors and the denominator the length of the control string. Don't reduce this fraction to a simpler expression.

The string has a length greater or equal to one and contains only letters from ato z.

Examples:
s="aaabbbbhaijjjm"
printer_error(s) => "0/14"

s="aaaxbbbbyyhwawiwjjjwwm"
printer_error(s) => "8/22"

"""
import string
def printer_error(s):
    letters = list(string.ascii_lowercase)
    unwanted_letters = []

    for letter in s:
        if letter not in letters:
            unwanted_letters.append(letter)

    return "{0}/{1}".format(len(unwanted_letters),len(s))

s="aaabbbbhaijjjm"
print(printer_error(s))
s="aaaxbbbbyyhwawiwjjjwwm"
print(printer_error(s))

# ------------------------------------------------
"""
Simple, given a string of words, return the length of the shortest word(s).

String will never be empty and you do not need to account for different data types.

Examples
(" I will make bitcoin take over the world maybe who knows perhaps"), 1)
("turns out random test cases are easier than writing out basic ones"), 3)

"""

def find_short(s):
    # create a list of length of words
    len_list = [len(word) for word in s.split()]

    # return the minimum value of the list
    return min(len_list)

s= "I will make bitcoin take over the world maybe who knows perhaps"
print(find_short(s))
s = "turns out random test cases are easier than writing out basic ones"
print(find_short(s))

# -------------------------------------------------------
"""Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case).

Examples
"the-stealth-warrior" gets converted to "theStealthWarrior"
"The_Stealth_Warrior" gets converted to "TheStealthWarrior"

"""