# Challenge:
#  Write a function to find the common elements between two lists.
# Instructions:
# Input: Two lists of integers (e.g., [1, 2, 3] and [2, 3, 4]).
# Output: A list of integers representing the intersection (e.g., [2, 3]).

def find_common_elements(list, elements):
    common = []
    for num in list:
        if num in elements:
            common.append(num)
            elements.remove(num)
    return common 
