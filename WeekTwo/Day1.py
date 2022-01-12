'''
The main idea is to count all the occurring characters in a string. If you have a string like aba, then the result should be {'a': 2, 'b': 1}.

What if the string is empty? Then the result should be empty object literal, {}.
'''
def count(string):
    list1 = list(string)
    
    count_dict = {x:list1.count(x) for x in list1}
    
    return count_dict

# print
string = 'aabcdeffgacb'
print(count(string))
empty_string = ''
print(count(empty_string))